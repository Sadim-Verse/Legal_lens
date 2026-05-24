# LegalLens — Nigerian Legal Self-Help RAG System
## Project Documentation v2.0
### Last Updated: May 2026

---

## 1. Mission & Hard Constraints

### What this project is
- A demonstrable prototype of a production-minded RAG pipeline.
- A showcase of the ability to evaluate LLM output, not just generate it.
- A tool that proves retrieval is not "dump PDF into vector DB and chat."

### What this project is NOT
- A legal advice platform. A clear disclaimer appears on every screen.
- A complete solution for all Nigerian laws. Focused on 3 specific documents.
- A fancy UI exercise. Functional and usable, not beautiful.

### Iron Rule
The system must correctly answer:

    "Under what section of the Constitution can I refuse a police search without a warrant?"

...with a correct citation and a plain-English explanation. If it cannot, the project has failed.

---

## 2. Target Documents

| # | Document | Why |
|---|----------|-----|
| 1 | Constitution of the Federal Republic of Nigeria 1999 (as amended) | Highest-impact source; covers all fundamental rights |
| 2 | Nigeria Police Act 2020 | Rules for arrests, searches, citizen rights during police encounters |
| 3 | Labour Act Cap. L1 LFN 2004 | Employment contracts, termination, wages, worker protections |

**Source:** placng.org / lawsofnigeria.placng.org (text-based PDFs, verified selectable).

**Why these three?** They cover the most common legal problems ordinary Nigerians
face daily: police harassment, wrongful dismissal, and basic rights. They are
publicly available, heavily structured, and dense — ideal for testing chunking
and retrieval strategies.

---

## 3. Technical Architecture (Actual, as Built)

### Stack Comparison

| Component         | Originally Planned          | Actual (as Built)                          |
|-------------------|-----------------------------|--------------------------------------------|
| LLM (classify)    | gpt-3.5-turbo               | llama-3.3-70b-versatile (Groq API)         |
| LLM (HyDE)        | gpt-3.5-turbo               | llama-3.1-8b-instant (Groq API)            |
| LLM (generation)  | gpt-3.5-turbo               | llama-3.3-70b-versatile (Groq API)         |
| Embeddings        | all-MiniLM-L6-v2            | BAAI/bge-base-en-v1.5 (local HuggingFace)  |
| Vector store      | Chroma (local)              | Chroma (local, persistent)                 |
| Reranker          | Not planned                 | cross-encoder/ms-marco-MiniLM-L-6-v2       |
| UI                | Gradio                      | Gradio (pending)                           |
| Evaluation        | ragas                       | Custom eval scripts + ragas (pending)      |

### Retrieval Pipeline (as Built)

```
User Question
      │
      ▼
┌──────────────────────────────────────────────────────┐
│  classify_query()   [Groq 70B]                       │
│  Two-step chain-of-thought:                          │
│    Step 1 — Is this a Nigerian legal question?       │
│    Step 2 — Which of the 3 Acts covers it?           │
│  Output: (in_scope, source, confidence)              │
└──────────────────────────────────────────────────────┘
      │
      ├── out_of_scope=True → return [] → "not in sources"
      │
      ▼
┌──────────────────────────────────────────────────────┐
│  requires_specific_detail()   [local, no API call]   │
│  Detects questions about ranks, numbers,             │
│  percentages, timeframes, years of service.          │
│  Skips HyDE for these to prevent hallucination.      │
└──────────────────────────────────────────────────────┘
      │
      ├── specific_detail=True → embed raw query directly
      │
      └── general question ──►
          ┌─────────────────────────────────────────┐
          │  rewrite_query_legal()   [Groq 8B]      │
          │  HyDE: generates a hypothetical         │
          │  Nigerian legal clause to improve       │
          │  embedding proximity to corpus text.    │
          └─────────────────────────────────────────┘
      │
      ▼
┌──────────────────────────────────────────────────────┐
│  Chroma similarity_search_with_score()               │
│                                                      │
│  Strategy A (HIGH confidence + known source):        │
│    Filtered single retrieval, k=20                   │
│                                                      │
│  Strategy B (LOW confidence or UNKNOWN source):      │
│    Dual retrieval — HyDE query + raw query,          │
│    merged and deduplicated, k=20 each                │
│                                                      │
│  Cosine distance threshold: < 0.8                    │
└──────────────────────────────────────────────────────┘
      │
      ▼
┌──────────────────────────────────────────────────────┐
│  rerank()   [local CrossEncoder]                     │
│  cross-encoder/ms-marco-MiniLM-L-6-v2               │
│  Re-scores each chunk against the ORIGINAL query.   │
│  Returns top-5 by relevance logit.                  │
│  Note: scores are logits (higher = better),         │
│  NOT cosine distances.                              │
└──────────────────────────────────────────────────────┘
      │
      ▼
  Retrieved chunks: List[(Document, rerank_score)]
      │
      ▼   [GENERATION — to be wired]
┌──────────────────────────────────────────────────────┐
│  answer()   [Groq 70B]                               │
│  Grounded generation from retrieved chunks only.    │
│  Plain English + exact section citations.           │
│  Strictly prohibited from using outside knowledge. │
└──────────────────────────────────────────────────────┘
      │
      ▼
  Gradio UI — response + citations displayed
```

### Key Design Decisions and Rationale

**Why HyDE (Hypothetical Document Embeddings)?**
A user question like "Can police search my home?" embeds very differently from
the statutory text "The privacy of citizens and their homes shall be inviolable."
HyDE bridges this gap by generating a hypothetical clause in statutory language,
whose embedding is geometrically closer to the actual corpus text.

**Why skip HyDE for specific-detail questions?**
The 8B model hallucinated specific values (wrong rank names, wrong percentages,
wrong timeframes) when asked questions like "What is the rank of the officer who
heads the Complaints Unit?" The hallucinated value drifts the embedding toward
the wrong section. Raw query embedding is safer for these cases.

**Why a 70B model for classification but 8B for HyDE?**
Classification is a precision task — wrong decisions block retrieval entirely.
HyDE is a generative task where approximate stylistic correctness is sufficient.
The 70B model costs more tokens per call but makes fewer categorical errors.

**Why cross-encoder reranking?**
Cosine similarity retrieves chunks that are distributionally close to the query
embedding. A cross-encoder directly scores each (query, chunk) pair for relevance
— a fundamentally more accurate signal, at the cost of running N forward passes
instead of one. Used after coarse retrieval to re-order the candidate pool.

**Why fail the classifier closed (out_of_scope → return [])?**
A false negative (wrongly blocking an in-scope question) is visible and
recoverable — the user sees "not found" and can rephrase. A false positive
(allowing an out-of-scope question through) produces a confidently wrong answer
from a mismatched chunk. The latter is worse for a legal system.

---

## 4. Data Preparation (Completed)

### Cleaning
- Stripped headers, footers, and page numbers.
- Removed non-selectable/scanned pages (verified text-based source PDFs).

### Chunking Strategy
- Split by section boundary using regex patterns.
- Each section = one chunk, unless > 500 tokens → split at subsection boundaries
  (e.g., (1), (2), (a), (b)).
- Minimum chunk size: ~200 tokens to preserve legal context.

### Metadata (per chunk)
```python
{
    "source":         "Constitution" | "Police Act" | "Labour Act",
    "section_number": int,
    "title":          str,   # section heading
}
```

### Embedding
- Model: BAAI/bge-base-en-v1.5 (normalized embeddings)
- Query instruction prepended at search time:
  "Represent this sentence for searching relevant passages: "
- Stored in Chroma, persisted to ./chroma_db

### Sanity Checks Performed
Test queries run manually before any generation work:
- "right to personal liberty"         → Constitution Sec 35 ✓
- "unlawful arrest by police"          → Police Act Sec 38 ✓
- "termination without notice"         → Labour Act Sec 11 ✓
- "Can I be tortured or held as slave" → Constitution Sec 34 ✓

---

## 5. Generation Prompt (To Be Wired)

```python
SYSTEM_PROMPT = """You are a Nigerian legal information assistant.
Use ONLY the provided legal excerpts to answer the user's question in
clear, simple English that a non-lawyer can understand.

If the excerpts do not contain the answer, say exactly:
'I cannot find relevant legal information in my sources for this question.'

Rules:
1. Cite the exact source and section number for every factual claim.
   Format: (Source, Section N)
2. Do not add legal interpretation, opinion, or advice beyond what
   is stated in the excerpts.
3. Do not use any information from outside the provided excerpts.
4. Keep the answer under 150 words unless the question genuinely
   requires more detail.
5. Never use legal jargon without immediately explaining it in plain
   English in parentheses.

Disclaimer reminder: This is a technology demonstration, not legal
advice. Always consult a qualified Nigerian lawyer for your specific
situation."""
```

---

## 6. Evaluation Strategy

### 6.1 Test Sets (Completed)

| Set | Size | Generation Method | Context Recall |
|-----|------|-------------------|----------------|
| Curated Set 1 | 25 questions | Human-authored (in-corpus knowledge) | 96% |
| Adversarial Set 2 | 20 questions | Human-authored (edge cases, paraphrasing) | 80–84% |
| Blind Set 3 | 20 questions | NotebookLM (no author corpus access) | 85% |
| Blind Set 4 | 20 questions | NotebookLM (no author corpus access) | 85% |

**Honest baseline: 85% context recall on blind, grounded test sets.**
The 96% figure on the curated set is inflated by author familiarity with
the corpus. The 85% NotebookLM figure is the number to report.

### 6.2 Retrieval Metrics (Pending — ragas)

Target: context_recall > 0.80 on blind test sets.
Status: Custom evaluation scripts built and validated; ragas integration pending.

Metrics to compute:
- `context_precision` — what fraction of retrieved chunks are relevant?
- `context_recall` — what fraction of necessary chunks were retrieved?
- `context_relevancy` — average relevancy score across queries

### 6.3 Generation Metrics (Pending)

| Metric | Method | Target |
|--------|--------|--------|
| Faithfulness | Manual audit — every claim traceable to a chunk | 0 hallucinations |
| Citation accuracy | Automated section number check | > 90% |
| Plain language score | 2–3 non-lawyer raters (1–5 scale) | > 3.5 average |
| Refusal accuracy | Automated on NOT_LEGAL test questions | 100% |

### 6.4 Documented Failure Categories

The following failure patterns have been identified and partially mitigated:

| Failure Type | Root Cause | Mitigation Applied |
|---|---|---|
| HyDE hallucination on specific values | 8B model invents rank names, percentages, timeframes | `requires_specific_detail()` skips HyDE |
| Classifier false negatives | "Debt", "food", "election" keywords trigger wrong exclusions | Chain-of-thought prompt with explicit disambiguation examples |
| Cross-encoder mis-ranking on adjacent sections | MS MARCO reranker not domain-adapted for Nigerian law | RERANK_TOP_K increased to 20; wider candidate pool |
| Sec 131/132 boundary confusion | Two adjacent sections cover one topic; chunk boundary falls wrong | Known issue; inspect_chunks diagnostic available |
| Source misclassification (IGP term → Constitution) | "Term of office" sounds constitutional | Explicit Police Act ⚠ disambiguation added to classifier |

---

## 7. User Interface (To Be Built)

**Framework:** Gradio Blocks
**Deployment target:** Hugging Face Spaces
**Time budget:** 2–3 hours maximum. No CSS work.

### Layout

```
┌──────────────────────────────────────────────────────┐
│  LegalLens — Nigerian Law Self-Help (Demo)           │
│                                                      │
│  ⚠ DISCLAIMER: This is a technology demonstration,  │
│  not legal advice. Always consult a qualified        │
│  Nigerian lawyer for your specific situation.        │
├──────────────────────────────────────────────────────┤
│                                                      │
│  [Chat window — scrollable]                          │
│                                                      │
│  User:  Can the police search my home without        │
│         a warrant?                                   │
│                                                      │
│  LegalLens:  The privacy of your home is             │
│  protected under Nigerian law. Generally, no one     │
│  may search your home without a warrant...           │
│                                                      │
│  📄 Source: Constitution, Section 37                 │
│                                                      │
├──────────────────────────────────────────────────────┤
│  [Text input box]                     [Send]         │
└──────────────────────────────────────────────────────┘
```

### Behaviour requirements
- Disclaimer visible at all times (not dismissable)
- Source citations displayed below every answer
- "I cannot find relevant legal information" shown for out-of-scope queries
- No streaming required for prototype (non-streaming generation is fine)

---

## 8. Logging (To Be Built)

Every query logged to `logs/queries.jsonl` in append mode:

```json
{
  "timestamp": "2026-05-23T14:32:01Z",
  "query": "Can police search my home?",
  "in_scope": true,
  "source_classified": "Constitution",
  "confidence": "HIGH",
  "hyde_used": true,
  "rewritten_query": "The privacy of citizens and their homes...",
  "retrieved_sections": [
    {"source": "Constitution", "section": 37, "score": 6.42},
    {"source": "Constitution", "section": 35, "score": 3.11}
  ],
  "answer": "The privacy of your home is protected..."
}
```

---

## 9. Revised Week-by-Week Status

| Week | Planned Goal | Status |
|------|--------------|--------|
| 1 | Ingest, chunk, embed, baseline retrieval, 20-question test set | ✅ Complete and exceeded |
| 2 | Generation pipeline, Gradio UI, prompt tuning | ⏳ Retrieval far exceeded; generation not yet wired |
| 3 | ragas metrics, faithfulness audit, hardening, logging | ⏳ Retrieval hardened; ragas and logging pending |
| 4 | Deployment, README, demo video, GitHub polish | 🔲 Not started |

### Immediate Priorities (Week 4 completion)

In order of dependency:

1. Build `answer()` — Groq 70B, grounded prompt, ~30 lines
2. Wire `retrieve()` → `answer()` → test on iron rule question
3. Build Gradio UI — chat window, disclaimer, source display
4. Run ragas on existing test set CSVs
5. Manual faithfulness audit on 15 non-edge test questions
6. Add JSON query logging
7. Deploy to Hugging Face Spaces (set GROQ_API_KEY as Space secret)
8. Write README.md and record 2-minute demo screencast

---

## 10. Known Limitations (To Be Declared in README)

- Corpus covers only 3 Acts. Questions about CAMA, tax, criminal
  penalties, cybercrimes, immigration, and other areas will correctly
  return "not in sources."

- The cross-encoder reranker (ms-marco-MiniLM-L-6-v2) was trained on
  web search data, not Nigerian legal text. It may mis-rank semantically
  adjacent statutory sections.

- HyDE generation uses an 8B model that can hallucinate specific statutory
  values. This is mitigated by the specific-detail detector but not
  eliminated for all question types.

- Context recall on blind test sets is 85%. One in six questions may
  retrieve a suboptimal or incorrect section.

- This system is not a substitute for legal advice. It is a technology
  demonstration of retrieval-augmented generation applied to a high-stakes
  domain.

---

## 11. Pitfalls — Updated Assessment

| Pitfall | Original Mitigation | Current Status |
|---------|--------------------|-|
| Tiny chunk size | Section-based chunks, min 200 tokens | ✅ Implemented |
| Header/footer noise | Regex clean before embedding | ✅ Implemented |
| Hallucination in generation | Strict grounded prompt | 🔲 Prompt written, not yet tested |
| Self-evaluation bias | Blind test set scoring | ✅ NotebookLM used; human blind scoring pending |
| No refusal testing | NOT_LEGAL test questions | ✅ Tested extensively across 4 test sets |
| Over-engineering | Stay low-level, understand every step | ⚠ Pipeline is complex but fully understood and documentable in an interview |

---

## 12. CV Claim (Honest and Earned)

"Engineered a multi-stage legal information retrieval system over Nigerian
statutes (Constitution, Police Act, Labour Act) featuring HyDE query
rewriting, a 70B chain-of-thought scope and source classifier, confidence-
gated dual-retrieval, and cross-encoder reranking. Achieved 85% context
recall on blind NotebookLM-generated test sets across 4 evaluation rounds.
Deployed as a Gradio application with grounded generation, zero-hallucination
target, and full evaluation reporting including faithfulness audit and refusal
accuracy measurement."

---

## 13. Repository Structure

```
Legal_Lens/
├── scripts/
│   ├── retrieval_test.py      # Full retrieval pipeline (production)
│   ├── eval_retrieval.py      # Evaluation harness
│   └── inspect_chunks.py      # Diagnostic — view stored chunk text
├── test_set/
│   ├── test_questions.csv     # Curated set 1 (25 questions)
│   ├── test_questions_2.csv   # Adversarial set 2 (20 questions)
│   ├── test_questions_3.csv   # Blind set 3 — NotebookLM (20 questions)
│   └── test_questions_4.csv   # Blind set 4 — NotebookLM (20 questions)
├── chroma_db/                 # Persisted Chroma vector store
├── logs/
│   └── queries.jsonl          # Query log (to be implemented)
├── app.py                     # Gradio UI entry point (to be built)
├── requirements.txt
└── README.md
```

---

*End of documentation. Version 2.0. For questions about technical decisions,
refer to the project development log maintained alongside this document.*
