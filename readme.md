# ⚖️ LegalLens — Know Your Nigerian Rights

> A retrieval-augmented generation system that answers plain-English questions
> about Nigerian law, cited directly from statute.

**Live demo:** [Hugging Face Spaces](#) *(link after deployment)*

---

## ⚠️ Disclaimer

This is a technology demonstration, not legal advice.
Always consult a qualified Nigerian lawyer for your specific situation.
LegalLens covers only three sources: the Nigerian Constitution (1999),
the Police Act 2020, and the Labour Act.

---

## What it does

Ask LegalLens a question in plain English:

> *"Can the police search my home without a warrant?"*

It finds the relevant Nigerian legal provision, explains it clearly,
and cites the exact section:

> *"The Constitution guarantees the privacy of citizens and their homes
> under Section 37 (Right to private and family life). A search without
> a warrant would be a violation of this constitutional right."*
>
> Source: Constitution, Section 37 — Right to private and family life

---

## Why this is hard

Most RAG tutorials connect a PDF to a vector database and call it done.
Legal text breaks that approach in several ways:

**The vocabulary gap.** A user asks "Can police search my home?"
The statute says "The privacy of citizens, their homes... is hereby
guaranteed and protected." These embed very differently.
Without bridging that gap, the retriever never finds Section 37.

**Short sections lose to long ones.** Section 37 is 17 words.
Section 36 (fair hearing) is 856 words across 12 subsections.
In embedding space, the longer section dominates almost every
constitutional query — even when it's the wrong answer.

**Hallucination on specific values.** A generative query rewriter
will invent wrong rank names, wrong percentages, wrong timeframes.
The fix is not a better prompt — it's detecting which question
types to skip rewriting for entirely.

---

## Architecture

```
User Question
      │
      ▼
┌─────────────────────────────────────────────┐
│  classify_query()   [Groq 70B]              │
│  Two-step chain-of-thought:                 │
│  1. Is this a Nigerian legal question?      │
│  2. Which of the 3 Acts covers it?          │
│  Output: (in_scope, source, confidence)     │
└─────────────────────────────────────────────┘
      │ out_of_scope → "not in sources"
      ▼
┌─────────────────────────────────────────────┐
│  requires_specific_detail()   [local]       │
│  Detects rank/number/timeframe questions.   │
│  Skips HyDE for these, to prevent           │
│  factual hallucination.                     │
└─────────────────────────────────────────────┘
      │
      ├── specific detail → embed raw query
      │
      └── general question →
          rewrite_query_legal()   [Groq 8B]
          HyDE: hypothetical Nigerian legal
          clause → closer to corpus embedding
      │
      ▼
┌─────────────────────────────────────────────┐
│  Chroma similarity_search_with_score()      │
│  HIGH confidence + known source →           │
│    filtered retrieval (k=5)                 │
│  LOW confidence or UNKNOWN →                │
│    dual retrieval: HyDE + raw, merged       │
└─────────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────┐
│  rerank()   [CrossEncoder, local]           │
│  ms-marco-MiniLM-L-6-v2                     │
│  Re-scores chunks vs original query        │
└─────────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────────┐
│  answer()   [Groq 70B]                      │
│  Grounded generation — no outside           │
│  knowledge, exact section citations,        │
│  plain English                              │
└─────────────────────────────────────────────┘
```

### Key design decisions

| Decision | Why |
|---|---|
| 70B model for classification | Precision matters — wrong classification blocks retrieval entirely |
| 8B model for HyDE | Speed matters — stylistic approximation is sufficient |
| Skip HyDE for specific-detail questions | 8B model hallucinates specific values (ranks, percentages, timeframes) |
| Chunk enrichment for short sections | 17-word Section 37 was invisible without keyword expansion |
| Fail classifier closed | False negatives are visible; false positives produce confident wrong answers |
| Eager model loading | Eliminates 7.7s cold-start penalty on first query |

---

## Corpus

| Source | Coverage |
|---|---|
| Constitution of the Federal Republic of Nigeria 1999 (as amended) | Fundamental rights, governance structure, legislative qualifications |
| Nigeria Police Act 2020 | Arrest powers, search, custody, citizen rights, officer misconduct |
| Labour Act Cap. L1 LFN 2004 | Employment contracts, wages, leave, termination, child labour |

---

## Evaluation

Four evaluation rounds, 85 test questions total.

| Test Set | Size | Method | Context Recall |
|---|---|---|---|
| Curated Set 1 | 25 | Human-authored (in-corpus knowledge) | 96% |
| Adversarial Set 2 | 20 | Human-authored (edge cases) | 84% |
| Blind Set 3 | 20 | NotebookLM — no author corpus access | 85% |
| Blind Set 4 | 20 | NotebookLM — no author corpus access | 85% |

**Honest baseline: 85% on blind test sets.**
The 96% figure on the curated set is inflated by author familiarity
with the corpus. The NotebookLM figure is the number to cite.

### Documented failure categories

| Failure | Root cause | Mitigation |
|---|---|---|
| HyDE hallucination on specific values | 8B model invents ranks/numbers | `requires_specific_detail()` skips HyDE |
| Classifier false negatives | "debt", "food", "elections" keywords trigger wrong exclusions | Chain-of-thought prompt with disambiguation examples |
| Short sections invisible in retrieval | 17-word chunk loses to 856-word chunk | Keyword enrichment appended to short sections |
| Cross-encoder mis-ranking | MS MARCO reranker not domain-adapted | RERANK_TOP_K tuned; wider candidate pool |

---

## Performance

Measured on local CPU (Intel, no GPU):

| Step | Time |
|---|---|
| Scope + source classification (Groq 70B) | ~0.9s |
| HyDE rewriting (Groq 8B) | ~0.5s |
| Vector search (Chroma, local) | ~0.5s |
| Cross-encoder rerank (5 candidates, CPU) | ~0.4s |
| Grounded generation (Groq 70B) | ~0.9s |
| **Total** | **~3.2s** |

Models are pre-loaded at startup to eliminate cold-start penalty.

---

## Stack

| Component | Technology |
|---|---|
| LLM (classify + generate) | `llama-3.3-70b-versatile` via Groq API |
| LLM (HyDE rewriting) | `llama-3.1-8b-instant` via Groq API |
| Embeddings | `BAAI/bge-base-en-v1.5` (local, HuggingFace) |
| Vector store | Chroma (local, persistent) |
| Reranker | `cross-encoder/ms-marco-MiniLM-L-6-v2` (local) |
| UI | Gradio 5.x |
| Deployment | Hugging Face Spaces |

---

## Project structure

```
Legal_Lens/
├── app.py                          # Gradio UI entry point
├── scripts/
│   ├── retrieval_test.py           # Full retrieval pipeline
│   ├── generation.py               # Grounded generation
│   ├── build_police_act.py         # Convert the current police act pdf into a text selectable one
│   ├── clean_and_chunk.py          # PDF cleaning and section parsing
│   ├── clean_police_act.py         # PDF cleaning and section parsing for Police act
│   ├── clean_labour_act.py         # PDF cleaning and section parsing for Labour act
│   ├── embed_and_index.py          # Chunking, enrichment, and indexing
│   └── eval_retrieval.py           # Evaluate csv files of test questions
├── test_set/
│   ├── test_questions.csv          # Curated set (25 questions)
│   ├── test_questions_2.csv        # Adversarial set (20 questions)
│   ├── test_questions_3.csv        # Blind set 3 — NotebookLM
│   └── test_questions_4.csv        # Blind set 4 — NotebookLM
├── data/
│   ├── raw/                        # Original PDFs
│   └── cleaned/                    # Parsed section JSONs
├── chroma_db/                      # Persisted vector store
├── requirements.txt
├── .env                            # Local only — never committed
└── README.md
```

---

## Local setup

```bash
# Clone the repository
git clone https://github.com/Sadim-Verse/legallens
cd legallens

# Create and activate virtual environment
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your Groq API key
echo "GROQ_API_KEY=your_key_here" > .env

# Run the app
python app.py
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

---

## Known limitations

- Corpus covers only 3 Acts. Questions about CAMA, tax, criminal
  penalties, cybercrimes, and immigration correctly return
  "not in sources."
- The cross-encoder reranker was trained on web search data, not
  Nigerian legal text. It may mis-rank semantically adjacent sections.
- Context recall is 85% on blind test sets — one in six questions
  may retrieve a suboptimal section.
- This system is not a substitute for legal advice.

---

## Author

Built by [Ibraheem](https://github.com/Sadim-Verse) —
CS student at Osun State University, ML & Game AI developer.

*Interested in the intersection of AI, African contexts,
and political economy.*