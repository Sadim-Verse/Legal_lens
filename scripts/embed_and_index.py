"""
Load sections from multiple JSON files, apply token-based chunking,
embed with BAAI/bge-base-en-v1.5, and persist to a single Chroma index.
"""

import json, re, os, shutil
import tiktoken
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

enc = tiktoken.get_encoding("cl100k_base")

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
    # Load all available statute JSONs 
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

    # Chunk
    all_chunks = []
    for sec in all_sections:
        all_chunks.extend(chunk_section(sec))
    print(f"Total chunks after token-aware splitting: {len(all_chunks)}")

    # Embed
    print("Initializing embedding model (BAAI/bge-base-en-v1.5) ...")
    embedding = HuggingFaceEmbeddings(
        model_name="BAAI/bge-base-en-v1.5",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    print("Embedding model loaded.")

    # Build document objects
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

    # Wipe old index and persist fresh 
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