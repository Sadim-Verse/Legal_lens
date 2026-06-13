"""
Generation layer for LegalLens.

Takes retrieved chunks from retrieval_test.retrieve() and produces
a grounded plain-English answer with exact section citations.

Single Groq 70B call. Strictly grounded — no outside knowledge used.
"""

import os
os.environ["TQDM_DISABLE"] = "1"
os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import warnings
warnings.filterwarnings("ignore")

import logging
import time
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)

from groq import Groq
from dotenv import load_dotenv
load_dotenv()


# Configuration
GENERATION_MODEL  = "llama-3.3-70b-versatile"
MAX_ANSWER_TOKENS = 400
MAX_CONTEXT_CHUNKS = 3   # top-3 of the 5 retrieved; avoids prompt bloat

SYSTEM_PROMPT = """You are a Nigerian legal information assistant called LegalLens.

Your ONLY job is to answer the user's question using the legal excerpts provided.
Explain the answer in clear, simple English that a non-lawyer can understand.

STRICT RULES:
1. Use ONLY the provided excerpts. Do not use any outside knowledge.
2. Cite the exact source and section for every factual claim.
   Format: (Source, Section N)
3. If the excerpts do not contain enough information to answer, say exactly:
   "I cannot find relevant legal information in my sources for this question."
4. Do not give legal advice, opinions, or interpretation beyond what the
   excerpts state.
5. Never use legal jargon without immediately explaining it in plain English.
6. Keep the answer under 150 words unless the question genuinely requires more.
7. End every response with:
   "DISCLAIMER: This is a technology demonstration, not legal advice.
   Always consult a qualified Nigerian lawyer for your specific situation.
8. Never use words like 'implying', 'suggesting', or 'indicating'.
    State what the law says directly.
9. When a constitutional right clearly implies a protection, state the 
    implication plainly. Do not hedge with 'does not explicitly state'.""

Answer format:
- Lead with the direct answer in one sentence.
- Follow with the explanation and citation.
- Close with the disclaimer."""

# Groq client
groq_client = Groq(api_key=os.environ["GROQ_API_KEY"])


# Context builder
def build_context(results: list) -> str:
    """
    Converts top retrieved chunks into a numbered context string
    for the generation prompt.

    Uses only top MAX_CONTEXT_CHUNKS to avoid prompt bloat while
    preserving the most relevant provisions.
    """
    if not results:
        return ""

    context_parts = []
    for i, (doc, score) in enumerate(results[:MAX_CONTEXT_CHUNKS]):
        source  = doc.metadata.get("source", "Unknown")
        section = doc.metadata.get("section_number", "?")
        title   = doc.metadata.get("title", "")
        text    = doc.page_content.strip()

        context_parts.append(
            f"[Excerpt {i+1}]\n"
            f"Source: {source}, Section {section}"
            + (f" — {title}" if title else "")
            + f"\n{text}"
        )

    return "\n\n".join(context_parts)


# Citation extractor
def extract_citations(results: list) -> list[dict]:
    citations = []
    seen_sections = set()
    for doc, score in results:
        source  = doc.metadata.get("source", "Unknown")
        section = str(doc.metadata.get("section_number", "?"))
        key = (source, section)
        if key not in seen_sections:
            seen_sections.add(key)
            citations.append({
                "source":  source,
                "section": section,
                "title":   doc.metadata.get("title", ""),
                "score":   round(float(score), 4),
            })
        if len(citations) == MAX_CONTEXT_CHUNKS:
            break
    return citations


# Main generation function
def answer(query: str, results: list) -> tuple[str, list[dict]]:
    """
    Generates a grounded plain-English answer from retrieved chunks.

    Args:
        query   : the original user question (not the rewritten HyDE clause)
        results : list of (Document, rerank_score) from retrieve()

    Returns:
        (answer_text, citations)
        answer_text : plain-English response with inline citations
        citations   : list of dicts for UI source display
    """
    # No results -> out of scope or nothing found
    if not results:
        return (
            "I cannot find relevant legal information in my sources "
            "for this question.\n\n"
            "DISCLAIMER: This is a technology demonstration, not legal advice. "
            "Always consult a qualified Nigerian lawyer for your specific situation.",
            []
        )

    context    = build_context(results)
    citations  = extract_citations(results)

    user_message = (
        f"Legal excerpts:\n\n{context}\n\n"
        f"User question: {query}"
    )

    try:
        t0 = time.perf_counter()
        response = groq_client.chat.completions.create(
            model=GENERATION_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_message},
            ],
            temperature=0.1,
            max_tokens=MAX_ANSWER_TOKENS,
        )
        t1 = time.perf_counter()
        print(f"[TIMER] answer() Groq call:    {t1-t0:.2f}s")
        answer_text = response.choices[0].message.content.strip()
        return answer_text, citations

    except Exception as e:
        print(f"[WARN] Generation failed ({e}).")
        return (
            "I was unable to generate an answer at this time. Please try again.\n\n"
            "DISCLAIMER: This is a technology demonstration, not legal advice. "
            "Always consult a qualified Nigerian lawyer for your specific situation.",
            citations
        )


# CLI for manual testing
if __name__ == "__main__":
    import sys
    from retrieval_test import retrieve

    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else \
        "Can the police search my home without a warrant?"

    print(f"Question: {query}\n")
    print("=" * 60)

    results      = retrieve(query, k=5)
    answer_text, citations = answer(query, results)

    print("\nANSWER:")
    print(answer_text)

    print("\nSOURCES:")
    for c in citations:
        print(f"  -> {c['source']}, Section {c['section']}"
              + (f" — {c['title']}" if c['title'] else ""))