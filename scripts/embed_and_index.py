"""
Load sections from multiple JSON files, apply token-based chunking,
enrich short single-chunk sections with keyword expansion,
embed with BAAI/bge-base-en-v1.5, and persist to a single Chroma index.

Changelog:
- Added ENRICHMENT_MAP for short sections that fail retrieval due to
  vocabulary mismatch between user queries and sparse statutory text
- Added enrich_chunk() applied after chunking, before embedding
- All other logic unchanged
"""

import json, re, os, shutil
import tiktoken
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

enc = tiktoken.get_encoding("cl100k_base")

# ── Enrichment map ─────────────────────────────────────────────────────────────
# Sections that are too short to match user queries reliably in embedding space.
# Keywords are appended to the chunk text before embedding — they are NOT shown
# to the user and do NOT modify the source JSON files.
# Format: (source, section_number): [keywords]

ENRICHMENT_MAP = {
    # Constitution
    ("Constitution", "37"): [
        "search", "warrant", "home search", "police search",
        "refuse search", "unlawful search", "right to privacy",
        "inviolable", "correspondence", "private life",
        "search without warrant", "can police search my home",
    ],
    ("Constitution", "43"): [
        "property", "land", "own property", "acquire property",
        "right to property", "immovable property",
        "can government take my land", "seize property",
    ],

    # Police Act
    ("Police Act", "33"): [
        "how to arrest", "making arrest", "physical arrest",
        "touch suspect", "body of suspect", "mode of arrest",
    ],
    ("Police Act", "34"): [
        "handcuff", "restraint", "bound", "no handcuffs",
        "when can police handcuff", "restrain suspect",
        "unnecessary restraint",
    ],
    ("Police Act", "36"): [
        "arrest in lieu", "cannot arrest instead", "wrong person",
        "substitute arrest", "arrested for someone else",
        "arresting wrong person",
    ],
    ("Police Act", "37"): [
        "humane treatment", "dignity", "abuse in custody",
        "treatment of suspect", "physical abuse",
        "police brutality", "torture arrest",
        "rights while arrested",
    ],
    ("Police Act", "39"): [
        "citizen arrest", "private person arrest", "civilian arrest",
        "anyone can arrest", "ordinary person arrest",
        "non police arrest", "regular citizen arrest",
    ],
    ("Police Act", "54"): [
        "racial profiling", "stop and search race",
        "discriminatory arrest", "colour hairstyle appearance",
        "cannot arrest because of looks", "no reasonable suspicion",
        "profiling", "targeted arrest",
    ],
    ("Police Act", "95"): [
        "police business", "officer private job",
        "conflict of interest", "police side job",
        "police trade", "police officer running business",
    ],
    ("Police Act", "132"): [
        "complaints unit rank", "PCRU head",
        "police complaints response unit composition",
        "chief superintendent", "who heads complaints unit",
        "rank of complaints officer",
    ],

    # Labour Act
    ("Labour Act", "3"): [
        "wages in liquor", "salary in alcohol",
        "paid in goods", "payment in kind",
        "wages in food", "not cash payment",
        "salary not money", "employer pay food",
    ],
}


def enrich_chunk(chunk: dict) -> dict:
    """
    Appends keyword expansion to short single-chunk sections.
    Only modifies the text used for embedding — source JSON is untouched.
    The appended keywords are hidden from the user; only page_content
    stored in Chroma is affected.
    """
    key = (chunk['source'], str(chunk['section_number']))
    if key in ENRICHMENT_MAP:
        keywords = ", ".join(ENRICHMENT_MAP[key])
        chunk = chunk.copy()
        chunk['text'] = chunk['text'] + f"\n\n[Related: {keywords}]"
    return chunk


def chunk_section(section, max_tokens=500, min_tokens=20):
    content = section['content']
    tokens = enc.encode(content)
    if len(tokens) <= max_tokens:
        return [{
            'text': content,
            'source': section['source'],
            'section_number': section['section_number'],
            'title': section['title'],
            'chunk_type': 'full_section'
        }]
    chunks = []
    for part in re.split(r'(?=\(\d+\)|\([a-z]\))', content):
        part = part.strip()
        if part and len(enc.encode(part)) >= min_tokens:
            chunks.append({
                'text': part,
                'source': section['source'],
                'section_number': section['section_number'],
                'title': section['title'],
                'chunk_type': 'sub_section',
                'sub_index': len(chunks)
            })
    return chunks


if __name__ == "__main__":
    # ── Load all statute JSONs ─────────────────────────────────────────────────
    json_paths = [
        "data/cleaned/constitution_sections.json",
        "data/cleaned/police_act_sections.json",
        "data/cleaned/labour_act_sections.json",
    ]
    all_sections = []
    for path in json_paths:
        if os.path.exists(path):
            print(f"Loading sections from {path} ...")
            with open(path, "r", encoding="utf-8") as f:
                sections = json.load(f)
            print(f"  -> {len(sections)} sections from {os.path.basename(path)}")
            all_sections.extend(sections)
        else:
            print(f"WARNING: {path} not found, skipping.")

    if not all_sections:
        raise RuntimeError("No section files loaded. Aborting.")

    print(f"\nTotal combined sections: {len(all_sections)}")

    # ── Chunk ──────────────────────────────────────────────────────────────────
    raw_chunks = []
    for sec in all_sections:
        raw_chunks.extend(chunk_section(sec))
    print(f"Total chunks after token-aware splitting: {len(raw_chunks)}")

    # ── Enrich short sections ──────────────────────────────────────────────────
    all_chunks = [enrich_chunk(c) for c in raw_chunks]
    enriched_count = sum(
        1 for c in all_chunks
        if "[Related:" in c['text']
    )
    print(f"Enriched {enriched_count} short sections with keyword expansion.")

    # ── Embed ──────────────────────────────────────────────────────────────────
    print("Initializing embedding model (BAAI/bge-base-en-v1.5) ...")
    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-base-en-v1.5",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    print("Embedding model loaded.")

    # ── Build Document objects ─────────────────────────────────────────────────
    # Note: page_content includes enrichment keywords for embedding quality.
    # metadata contains only clean statutory fields for display.
    docs = []
    for c in all_chunks:
        docs.append(Document(
            page_content=f"Section {c['section_number']} - {c['title']}: {c['text']}",
            metadata={
                'source': c['source'],
                'section_number': c['section_number'],
                'title': c['title'],
                'chunk_type': c['chunk_type'],
                'sub_index': c.get('sub_index', -1)
            }
        ))
    print(f"Prepared {len(docs)} document objects.")

    # ── Wipe old index and persist fresh ──────────────────────────────────────
    persist_dir = "./chroma_db"
    if os.path.exists(persist_dir):
        shutil.rmtree(persist_dir)
        print(f"Deleted existing index at {persist_dir}")

    print(f"Creating Chroma index and saving to {persist_dir} ...")
    vectorstore = Chroma.from_documents(
        docs, embedding, persist_directory=persist_dir
    )
    print(f"Successfully persisted {len(all_chunks)} chunks to {persist_dir}")

    if os.path.exists(persist_dir):
        print(f"Directory '{persist_dir}' exists on disk.")
    else:
        print("ERROR: chroma_db was not created.")