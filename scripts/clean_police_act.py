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

def parse_arrangement(raw_text):
    """
    Extract the official section titles from the 'Arrangement of Sections' block.
    Uses the second 'PART I - PRELIMINARY' as the end of the front matter.
    Returns a dict: section_number (str) -> title (str).
    """
    # Locate the start of the main Act (second PART I - PRELIMINARY)
    first_part = raw_text.find("PART I - PRELIMINARY")
    if first_part == -1:
        raise ValueError("Cannot find first 'PART I - PRELIMINARY'")
    second_part = raw_text.find("PART I - PRELIMINARY", first_part + 10)
    if second_part == -1:
        raise ValueError("Cannot find second 'PART I - PRELIMINARY' (main Act start)")

    # Front matter is everything before the second occurrence
    front_matter = raw_text[:second_part]
    start = front_matter.find("Arrangement of Sections")
    if start == -1:
        raise ValueError("Cannot find Arrangement of Sections in front matter")

    arrangement_text = front_matter[start:]

    # Pattern: optional whitespace, number, dot, whitespace, title (until end of line)
    pattern = r'^\s*(?P<num>\d+)\.\s+(?P<title>.+?)[.]?\s*$'
    mapping = {}
    for line in arrangement_text.split('\n'):
        m = re.match(pattern, line.strip())
        if m:
            num = m.group('num')
            title = m.group('title').strip().rstrip('.')
            mapping[num] = title
    return mapping

# Extract only the actual text
def extract_main_text(raw_text):
    # Find the second "PART I - PRELIMINARY"
    first = raw_text.find("PART I - PRELIMINARY")
    if first == -1:
        raise ValueError("Cannot find 'PART I - PRELIMINARY'")
    second = raw_text.find("PART I - PRELIMINARY", first + 10)
    if second == -1:
        raise ValueError("Cannot find second 'PART I - PRELIMINARY'")
    return raw_text[second:].strip()

# Clean headers and page numbers
def clean_police_act(text):
    # Remove the Act title that repeats on some pages
    text = re.sub(r'\nNIGERIA POLICE ACT, 2020\n', '\n', text)
    # Remove standalone page numbers
    text = re.sub(r'\n\d+\n', '\n', text)
    # Remove Part headers (e.g., "PART II – ESTABLISHMENT...")
    text = re.sub(r'\nPART\s+[IVXLCDM]+[^\n]*', '', text)
    # Collapse excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# Parse sections using regex
def parse_police_sections(clean_text, title_map):
    text = "\n" + clean_text
    # Capture section number and everything until the next section or end of file
    pattern = r'\n(?P<num>\d+)\.\s+(?P<body>.*?)(?=\n\d+\.\s+(?:[^\n]+\n)?|\Z)'
    matches = list(re.finditer(pattern, text, re.DOTALL))
    sections = []
    for m in matches:
        num = m.group('num')
        body = m.group('body').strip()
        if not body:
            continue
        # Use official title from arrangement, fallback to generic
        official_title = title_map.get(num, f"Section {num}")
        sections.append({
            'source': 'Police Act',
            'section_number': num,
            'title': official_title,
            'content': body
        })
    return sections

# Main execution, test
if __name__ == "__main__":
    pdf_path = "data/raw/Police_Act_2020.pdf"
    raw_text = load_pdf_text(pdf_path)
    
    # Get the official titles
    title_map = parse_arrangement(raw_text)
    
    # Extract only the real provisions
    main_text = extract_main_text(raw_text)
    cleaned = clean_police_act(main_text)
    
    # Parse sections with the correct titles
    sections = parse_police_sections(cleaned, title_map)
    print(f"Found {len(sections)} sections.")
    for sec in sections[:5]:
        print(f"Section {sec['section_number']}: {sec['title']}")
    
    # Save
    import json
    with open("data/cleaned/police_act_sections.json", "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2)
    print(f"Saved {len(sections)} sections to data/cleaned/police_act_sections.json")