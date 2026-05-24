"""
Retrieval pipeline:
1. Scope + source + confidence classifier  (Groq 70B, chain-of-thought)
2. Query-type detection                    (specific-detail vs general)
3. HyDE rewriting (general questions only) (Groq 8B)
   Raw query embedding (specific-detail questions — avoids hallucination)
4. Chroma vector search                    (filtered or dual-retrieval)
5. Distance threshold filter
6. Cross-encoder rerank                    (local)

Changelog vs previous version:
- Added requires_specific_detail() to detect questions about ranks,
  numbers, percentages, timeframes, named bodies, and ages
- HyDE is skipped for specific-detail questions; raw query is embedded
  directly — prevents factual hallucination from drifting the embedding
- All other logic unchanged
"""

import sys
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from groq import Groq
from sentence_transformers import CrossEncoder

# ── Configuration ──────────────────────────────────────────────────────────────
QUERY_INSTRUCTION    = "Represent this sentence for searching relevant passages: "
EMBEDDING_MODEL      = "BAAI/bge-base-en-v1.5"
CHROMA_DIR           = "./chroma_db"
SIMILARITY_THRESHOLD = 0.8
RERANK_TOP_K         = 10

VALID_SOURCES = {"Constitution", "Police Act", "Labour Act"}

# Linguistic patterns that signal a specific statutory fact is being asked for.
# HyDE is skipped for these — the 8B model will hallucinate the specific value.
SPECIFIC_DETAIL_SIGNALS = [
    "how many", "how much", "what is the maximum", "what is the minimum",
    "what is the rank", "what percentage", "within how many", "what age",
    "what timeframe", "how long", "what amount", "which body", "who heads",
    "what year", "how often", "what number", "what level", "what grade",
    "what is the penalty", "what fine", "how soon", "within what",
]

# ── Groq models ────────────────────────────────────────────────────────────────
CLASSIFIER_MODEL = "llama-3.3-70b-versatile"
HYDE_MODEL       = "llama-3.1-8b-instant"

groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])

# ── Lazy-loaded singletons ─────────────────────────────────────────────────────
_vectorstore = None
def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        embedding = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            encode_kwargs={"normalize_embeddings": True},
        )
        _vectorstore = Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=embedding,
        )
    return _vectorstore

_reranker = None
def get_reranker():
    global _reranker
    if _reranker is None:
        _reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    return _reranker


# ── Query-type detector ────────────────────────────────────────────────────────
def requires_specific_detail(question: str) -> bool:
    """
    Returns True if the question asks for a specific statutory fact
    (number, rank, named body, timeframe, percentage, age limit) where
    HyDE is structurally likely to hallucinate the specific value and
    drift the embedding toward the wrong section.

    For these questions, raw query embedding is used instead of HyDE.
    """
    lower = question.lower()
    return any(signal in lower for signal in SPECIFIC_DETAIL_SIGNALS)


# ── Layer 1: Scope + source + confidence classifier (70B) ─────────────────────
def classify_query(question: str) -> tuple[bool, str | None, str]:
    """
    Two-step chain-of-thought classifier.

    Returns: (in_scope, source, confidence)
      in_scope   : bool       — False → return [] immediately
      source     : str | None — 'Constitution' | 'Police Act' | 'Labour Act'
                                 None = UNKNOWN → dual retrieval, no filter
      confidence : str        — 'HIGH' | 'LOW'
                                 LOW → dual retrieval even if source is known
    """
    prompt = f"""You are a Nigerian legal classifier. Reason through two steps
before giving your final answer.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — Is this a Nigerian legal question at all?

Answer NO immediately and stop if the question involves ANY of:
  • Medication, medical treatment, or healthcare advice
  • Foreign countries or foreign law (e.g. US, UK, EU)
  • Stock markets, cryptocurrency, or capital gains tax
  • Patents, trademarks, or intellectual property
  • Building permits or construction regulations
  • Nigerian criminal penalties NOT found in the three Acts below
    (e.g. kidnapping sentences, cybercrime fines, EFCC investigations)

If none of the above apply, continue to Step 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2 — Is it covered by one of these three Acts?

CONSTITUTION (1999)
  Covers ALL of:
  • Fundamental rights: life, privacy, fair hearing, expression,
    religion/conscience, movement, association, discrimination,
    property and compulsory acquisition, personal liberty
  • Governance and structure: number of states, federal/state powers,
    declaration of emergency, language of legislature
  • Legislative qualifications and electoral provisions:
    minimum age to stand for election, senatorial districts,
    composition of legislative houses
  ⚠ "Electoral qualifications or governance structure" → IN SCOPE (Constitution)
  ⚠ "Election results or who won an election" → OUT OF SCOPE

POLICE ACT (2020)
  Covers ALL of:
  • Police powers: arrest (lawful and unlawful grounds), search,
    bail, custody, treatment of detained persons, interrogation rights
  • Citizen/private person arrest powers
  • Internal governance: ranks, appointments, special constables,
    police complaints units, disciplinary tribunals, police councils
  • Officer misconduct and discipline
  ⚠ "Arrested for owing a debt" → IN SCOPE (Police Act — unlawful arrest)
  ⚠ "Police Complaints Response Unit" → IN SCOPE (Police Act — internal governance)

LABOUR ACT (Cap. L1 LFN 2004)
  Covers ALL of:
  • Employment contracts, written terms, wage payment
  • Form of wages: must be legal tender — not goods, food, or vouchers
  • Wage advances, deductions, working hours
  • Annual leave, sick leave, maternity leave
  • Termination, notice periods, redundancy
  • Child labour, forced labour
  • Employer obligations on relocation
  • Exemptions: e.g. members of the armed forces or police
  ⚠ "Salary paid in goods or food" → IN SCOPE (Labour Act — form of payment)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DECISION RULES:
- If the question touches ANY coverage area above → YES
- When uncertain between YES and NO → prefer YES with LOW confidence
- When uncertain which single Act applies → SOURCE = UNKNOWN
- Output LOW confidence if you needed to reason carefully to decide

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Output EXACTLY three lines, nothing else:
IN_SCOPE: YES or NO
SOURCE: Constitution / Police Act / Labour Act / UNKNOWN
CONFIDENCE: HIGH or LOW

Question: "{question}"
Answer:"""

    try:
        response = groq_client.chat.completions.create(
            model=CLASSIFIER_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=20,
        )
        raw = response.choices[0].message.content.strip()

        lines = {}
        for line in raw.splitlines():
            if ":" in line:
                key, _, val = line.partition(":")
                lines[key.strip().upper()] = val.strip().upper()

        in_scope = lines.get("IN_SCOPE", "NO").startswith("YES")

        source_raw = lines.get("SOURCE", "UNKNOWN")
        if "POLICE" in source_raw:
            source = "Police Act"
        elif "LABOUR" in source_raw:
            source = "Labour Act"
        elif "CONSTITUTION" in source_raw:
            source = "Constitution"
        else:
            source = None

        confidence = "HIGH" if lines.get("CONFIDENCE", "LOW") == "HIGH" else "LOW"

        return in_scope, source, confidence

    except Exception as e:
        print(f"[WARN] Classifier failed ({e}). Defaulting to in-scope, all sources, LOW confidence.")
        return True, None, "LOW"


# ── Layer 2: HyDE clause generator (8B) ───────────────────────────────────────
def rewrite_query_legal(user_question: str) -> str:
    """
    Generates a hypothetical Nigerian legal clause for general questions.
    NOT called for specific-detail questions (see requires_specific_detail).
    """
    prompt = f"""You are a legal drafter writing a clause for a Nigerian statute or the Constitution.
The user is asking: "{user_question}"

Write a single formal clause (1 to 2 sentences) that directly answers the question.
Use the exact style of Nigerian legislation — sparse, declarative, present tense.

CRITICAL RULES:
1. Do NOT invent a blanket prohibition if the law allows the action conditionally.
   State the lawful conditions instead.
2. Match the register: constitutional syntax for rights questions
   ("Every person shall be entitled to...", "No person shall..."),
   statutory syntax for powers and procedures (Police Act / Labour Act style).
3. Use Nigerian legal language only: "lawful authority", "arrest without warrant",
   "shall be entitled to", "notwithstanding", "except as provided by law".
4. Do NOT mention section numbers.
5. Output ONLY the clause. No intro, no commentary, no explanation.
   If uncertain, write the closest plausible clause — never explain why
   you cannot answer.
6. If the question is about home privacy or searches of a dwelling, use the
   phrase "The privacy of citizens and their homes" explicitly.
7. If the question is about religious freedom or being compelled to follow a
   religion, use the phrase "freedom of thought, conscience and religion"
   explicitly.
8. If the question is about the right to remain silent or refusing to answer
   police questions, use the phrase "not be compelled to make any statement"
   explicitly.
9. If the question is about treatment of a person already in custody or
   detention, write about treatment in custody specifically — do NOT use
   "arrest without warrant" or reference arrest powers.
10. If the question involves a private citizen (not a police officer) making
    an arrest, use the phrase "any person other than a police officer"
    explicitly.
11. If the question is about informing a person of the reason for their arrest,
    use the phrase "informed of the reason for his arrest" explicitly.

Hypothetical Clause:"""

    try:
        response = groq_client.chat.completions.create(
            model=HYDE_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=120,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[WARN] HyDE rewrite failed ({e}). Falling back to raw query.")
        return user_question


# ── Deduplication ──────────────────────────────────────────────────────────────
def deduplicate(results: list) -> list:
    """
    Removes duplicate chunks by page_content.
    Keeps the lower (better) cosine distance for each unique chunk.
    """
    seen = {}
    for doc, score in results:
        key = doc.page_content
        if key not in seen or score < seen[key][1]:
            seen[key] = (doc, score)
    return list(seen.values())


# ── Layer 3: Cross-encoder reranker ───────────────────────────────────────────
def rerank(question: str, results: list, top_k: int = 5) -> list:
    """
    Re-scores chunks against the ORIGINAL user question.
    Returns top_k ordered by cross-encoder relevance (higher = more relevant).
    Scores are logits — NOT cosine distances.
    """
    if not results:
        return []
    reranker = get_reranker()
    pairs  = [(question, doc.page_content) for doc, _ in results]
    scores = reranker.predict(pairs)
    scored = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)
    return [(doc, float(score)) for (doc, _), score in scored[:top_k]]


# ── Main retrieval function ────────────────────────────────────────────────────
def retrieve(query: str, k: int = 5) -> list:
    """
    Full retrieval pipeline.
    Returns list of (Document, rerank_score) tuples, highest relevance first.
    Returns [] if query is out of scope or no relevant provisions found.
    """
    # ── 1. Classify ───────────────────────────────────────────────────────────
    in_scope, source, confidence = classify_query(query)

    if not in_scope:
        print("[INFO] Query is outside Nigerian legal scope.")
        return []

    print(f"[INFO] Classified → source: {source or 'ALL (UNKNOWN)'} | "
          f"confidence: {confidence}")

    # ── 2. Query-type detection + embedding ───────────────────────────────────
    if requires_specific_detail(query):
        print("[INFO] Specific-detail question — skipping HyDE, embedding raw query.")
        search_query = QUERY_INSTRUCTION + query
    else:
        legal_query  = rewrite_query_legal(query)
        print(f"[INFO] Original query : {query}")
        print(f"[INFO] Rewritten query: {legal_query}\n")
        search_query = QUERY_INSTRUCTION + legal_query

    vs = get_vectorstore()

    # ── 3. Retrieval strategy ─────────────────────────────────────────────────
    use_filter = source is not None and confidence == "HIGH"

    if use_filter:
        print(f"[INFO] Strategy: filtered retrieval ({source})")
        raw_results = vs.similarity_search_with_score(
            search_query,
            k=RERANK_TOP_K,
            filter={"source": source},
        )
    else:
        print("[INFO] Strategy: dual retrieval (HyDE + raw query, all sources)")
        hyde_results = vs.similarity_search_with_score(search_query,  k=RERANK_TOP_K)
        raw_results  = vs.similarity_search_with_score(
            QUERY_INSTRUCTION + query, k=RERANK_TOP_K
        )
        raw_results  = deduplicate(hyde_results + raw_results)

    # ── 4. Distance threshold filter ──────────────────────────────────────────
    raw_results = [r for r in raw_results if r[1] < SIMILARITY_THRESHOLD]

    if not raw_results:
        print("[INFO] No sufficiently relevant provision found.")
        return []

    # ── 5. Cross-encoder rerank against original query ────────────────────────
    reranked = rerank(query, raw_results, top_k=k)
    return reranked


# ── CLI ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    user_query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else \
        "Can I be tortured or held as a slave?"

    results = retrieve(user_query, k=5)

    if not results:
        print("[INFO] No results returned.")
    else:
        for i, (doc, score) in enumerate(results):
            print(f"--- Result {i+1} (rerank_score: {score:.4f}) ---")
            print(f"Source: {doc.metadata.get('source', '?')} | "
                  f"Section: {doc.metadata.get('section_number', '?')} | "
                  f"Title: {doc.metadata.get('title', '?')}")
            print(doc.page_content[:400])
            print()