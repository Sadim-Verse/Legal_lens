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
    Extract official section titles from the Arrangement of Sections block.
    The real law starts at the second 'PART I' (after the preamble).
    Everything before that is front matter.
    """
    # Find the start of the main Act: look for "PART I" that appears after "Commencement.]"
    start_marker = "Commencement.]"
    commence_idx = raw_text.find(start_marker)
    if commence_idx == -1:
        raise ValueError("Cannot find 'Commencement.]' marker")
    second_part = raw_text.find("PART I", commence_idx)
    if second_part == -1:
        raise ValueError("Cannot find second 'PART I' after Commencement]")

    front_matter = raw_text[:second_part]
    start = front_matter.upper().find("ARRANGEMENT OF SECTIONS")
    if start == -1:
        raise ValueError("Cannot find Arrangement of Sections in front matter")

    arrangement_text = front_matter[start:]

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
    # Find "Commencement.]" then the following "PART I"
    start_marker = "Commencement.]"
    commence_idx = raw_text.find(start_marker)
    if commence_idx == -1:
        raise ValueError("Cannot find 'Commencement.]'")
    second_part = raw_text.find("PART I", commence_idx)
    if second_part == -1:
        raise ValueError("Cannot find second 'PART I'")
    main_text = raw_text[second_part:].strip()

    # Remove everything from the Schedule heading onwards
    # Look for "SCHEDULE" that appears after the last section (92)
    # Use regex to find a line that starts with "SCHEDULE" (possibly with spaces)
    schedule_match = re.search(r'\n\s*SCHEDULE\s*\n', main_text)
    if schedule_match:
        main_text = main_text[:schedule_match.start()].strip()
    return main_text

# Clean headers and page numbers
def clean_labour_act(text):
    # Remove page headers
    text = re.sub(r'\n?CAP\.\s*L\d+\s*\nLabour Act\s*\n', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'\n?CHAPTER\s*L\d+\s*\nLABOUR ACT\s*\n', '\n', text, flags=re.IGNORECASE)
    # Remove issue markers like "Ll-51 [Issue 1]" or "Ll-4"
    text = re.sub(r'\nLl\-\d+\s*\[Issue \d+\]\s*\n', '\n', text)
    text = re.sub(r'\nLl\-\d+\s*\n', '\n', text)
    # Remove standalone "[Issue 1]" lines
    text = re.sub(r'\n\[Issue \d+\]\s*\n', '\n', text)
    # Collapse excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# Parse sections using regex
def parse_labour_sections(clean_text, title_map):
    text = "\n" + clean_text
    pattern = r'\n(?P<num>\d+)\.\s+(?P<body>.*?)(?=\n\d+\.\s+(?:[^\n]+\n)?|\Z)'
    matches = list(re.finditer(pattern, text, re.DOTALL))
    sections = []
    for m in matches:
        num = m.group('num')
        body = m.group('body').strip()
        if not body:
            continue
        # Stop if we have already processed section 92 (the last real section)
        if num == '92':
            # Add section 92 then break
            official_title = title_map.get(num, f"Section {num}")
            # Remove duplicated title line if present
            if body.startswith(official_title):
                body = body[len(official_title):].lstrip('\n').strip()
            sections.append({
                'source': 'Labour Act',
                'section_number': num,
                'title': official_title,
                'content': body
            })
            break

        official_title = title_map.get(num, f"Section {num}")
        if body.startswith(official_title):
            body = body[len(official_title):].lstrip('\n').strip()

        sections.append({
            'source': 'Labour Act',
            'section_number': num,
            'title': official_title,
            'content': body
        })
    return sections

# Main execution, test
if __name__ == "__main__":
    pdf_path = "data/raw/Labour_Act.pdf"
    raw_text = load_pdf_text(pdf_path)
    
    # Get the official titles
    title_map = parse_arrangement(raw_text)
    
    # Extract only the real provisions
    main_text = extract_main_text(raw_text)
    cleaned = clean_labour_act(main_text)
    
    # Parse sections with the correct titles
    sections = parse_labour_sections(cleaned, title_map)
    print(f"Found {len(sections)} sections.")
    for sec in sections[:5]:
        print(f"Section {sec['section_number']}: {sec['title']}")
    
    # Save
    import json
    with open("data/cleaned/labour_act_sections.json", "w", encoding="utf-8") as f:
        json.dump(sections, f, indent=2)
    print(f"Saved {len(sections)} sections to data/cleaned/labour_act_sections.json")