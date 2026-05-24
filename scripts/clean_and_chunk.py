"""
Load PDF, extract main text, clean, parse into sections, save sections to disk
"""

import json
import re
import tiktoken
from langchain_community.document_loaders import PyPDFLoader

# Load raw PDF text
def load_pdf_text(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    full_text = "\n".join([p.page_content for p in pages])
    return full_text

# Extract only the actual Constitution text (skip front matter)
def extract_main_text(raw_text):
    # Find the end of the preamble – allow line breaks and spaces
    match = re.search(
        r'DO\s+HEREBY\s+MAKE.*?following\s+Constitution:\s*',
        raw_text,
        re.DOTALL | re.IGNORECASE
    )
    if match:
        start_idx = match.end()
        return raw_text[start_idx:].strip()
    else:
        # Fallback: look for the second "CHAPTER I"
        first = raw_text.find("CHAPTER I")
        if first != -1:
            second = raw_text.find("CHAPTER I", first + 10)
            if second != -1:
                return raw_text[second:].strip()
        raise ValueError("Cannot locate real constitutional text.")

# Clean headers and page numbers
def clean_constitution(text):
    # Remove the repeating header (may be preceded by a lone page number)
    text = re.sub(
        r'\n?\d*\n?The Constitution of the Federal Republic of Nigeria Updated with the First, Second, Third, Fourth and Fifth Alterations\n',
        '\n',
        text
    )
    # Remove any remaining standalone page numbers (lines with only digits)
    text = re.sub(r'\n\d+\n', '\n', text)
    # Collapse excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# Parse sections using regex
def parse_constitution_sections(clean_text):
    # Ensure text starts with a newline so the first section is captured
    text = "\n" + clean_text
    pattern = r'\n(?P<num>\d+)\.\s+(?P<title>[^\n]+)\n(?P<body>.*?)(?=\n\d+\.\s+[A-Z]|\Z)'
    matches = list(re.finditer(pattern, text, re.DOTALL))
    sections = []
    for m in matches:
        num = m.group('num')
        title = m.group('title')
        body = m.group('body').strip()
        sections.append({
            'source': 'Constitution',
            'section_number': num,
            'title': title,
            'content': body
        })
    return sections

# Filter the sections to their actual amount
def filter_valid_sections(sections):
    valid = []
    seen = set()
    for s in sections:
        num = s['section_number']
        # Skip duplicates (shouldn't exist, but safe)
        if num in seen:
            continue
        # Accept only integer sections 1..320 or known lettered ones
        try:
            int(num)
            if 1 <= int(num) <= 320:
                valid.append(s)
                seen.add(num)
                continue
        except ValueError:
            pass
        # Accept known lettered sections (16A, 225A, 254A-F, etc.)
        if num in ['16A', '225A', '254A', '254B', '254C', '254D', '254E', '254F']:
            valid.append(s)
            seen.add(num)
    return valid



# Main execution, test
if __name__ == "__main__":
    pdf_path = "data/raw/Constitution.pdf"          # adjust if needed
    raw_text = load_pdf_text(pdf_path)
    print("Step 1 – Raw text loaded (first 500 chars):")
    # print(raw_text[:500])
    print("\n" + "="*80 + "\n")

    main_text = extract_main_text(raw_text)
    print("Step 2 – After extracting main text (first 1000 chars):")
    print(main_text[:1000])
    print("\n" + "="*80 + "\n")

    cleaned = clean_constitution(main_text)
    print("Step 3 – After cleaning headers/page numbers (first 1000 chars):")
    print(cleaned[:1000])
    print("\n" + "="*80 + "\n")

    sections = parse_constitution_sections(cleaned)
    sections = filter_valid_sections(sections)
    print(f"Step 4 – Found {len(sections)} sections.")
    # Show first 10 sections to verify
    for sec in sections[:10]:
        print(f"Section {sec['section_number']}: {sec['title']}")
    print("...")
    # Specifically check for Section 37
    sec37 = [s for s in sections if s['section_number'] == '37']
    if sec37:
        print("Section 37 found:", sec37[0]['title'])
    else:
        print("WARNING: Section 37 NOT FOUND – check regex or text.")
    print("\n" + "="*80 + "\n")

    # Print the body of a few sections
    for s in sections[:3]:
        print(f"Section {s['section_number']}: {s['content'][:200]}...")
    print("\n" + "="*80 + "\n")

    # Verify that the fundamental rights section is complete
    for s in sections:
        if int(s['section_number']) in range(33, 47):
            print(s['section_number'], s['title'])
    print("\n" + "="*80 + "\n")

    # Save sections to disk for the next script
    with open("data/cleaned/constitution_sections.json", "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2)
    print(f"Saved {len(sections)} sections to data/cleaned/constitution_sections.json")