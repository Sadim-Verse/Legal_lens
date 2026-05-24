# import csv
# from retrieval_test import retrieve


# def evaluate(test_csv_path: str):
#     with open(test_csv_path, "r", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         questions = list(reader)

#     hits = 0
#     soft_hits = 0  # section matched but fragment missing
#     total = len(questions)

#     print(f"{'='*80}")
#     print(f"Running evaluation on {total} questions...")
#     print(f"{'='*80}\n")

#     for row in questions:
#         question        = row['question'].strip()
#         expected_section  = row['expected_section'].strip()
#         expected_document = row['expected_document'].strip()
#         fragment          = row.get('ideal_answer_fragment', '').strip().lower()

#         results = retrieve(question, k=5)

#         # Build top-1 display string
#         if results:
#             top_doc, top_score = results[0]
#             top_info = (
#                 f"{top_doc.metadata.get('source', '?')} "
#                 f"Sec {top_doc.metadata.get('section_number', '?')} "
#                 f"(score {top_score:.4f})"
#             )
#         else:
#             top_info = "NO RESULTS / NOT_LEGAL"

#         # --- Section hit check ---
#         section_found = False
#         if expected_section.upper() == "NOT_LEGAL":
#             section_found = (len(results) == 0)
#         else:
#             for doc, _ in results:
#                 if (str(doc.metadata.get('section_number', '')) == expected_section and
#                         doc.metadata.get('source', '') == expected_document):
#                     section_found = True
#                     break

#         # --- Fragment check (skip for NOT_LEGAL rows) ---
#         fragment_found = True  # default pass if no fragment to check
#         if (expected_section.upper() != "NOT_LEGAL"
#                 and fragment
#                 and fragment != "not_legal"
#                 and results):
#             combined_text = " ".join(doc.page_content.lower() for doc, _ in results)
#             fragment_found = fragment in combined_text

#         # --- Scoring ---
#         if section_found and fragment_found:
#             hits += 1
#             print(f"  PASS       | {question[:65]:<65} → {top_info}")
#         elif section_found and not fragment_found:
#             soft_hits += 1
#             print(f"  PASS(soft) | {question[:65]:<65} → {top_info}  [fragment missing]")
#         else:
#             exp = (f"{expected_document} Sec {expected_section}"
#                    if expected_section.upper() != "NOT_LEGAL"
#                    else "NOT_LEGAL")
#             print(f"  FAIL       | {question[:65]:<65} → {top_info}  (expected {exp})")

#     # --- Summary ---
#     hard_recall = hits / total if total else 0
#     soft_recall = (hits + soft_hits) / total if total else 0

#     print(f"\n{'='*80}")
#     print(f"Hard Recall  (section + fragment): {hits}/{total} = {hard_recall:.2%}")
#     print(f"Soft Recall  (section only):       {hits + soft_hits}/{total} = {soft_recall:.2%}")
#     print(f"Target > 0.70 → {'✓ PASS' if hard_recall >= 0.70 else '✗ FAIL'}")
#     print(f"{'='*80}")


# if __name__ == "__main__":
#     evaluate("test_set/test_questions.csv")

import csv
from retrieval_test import retrieve

def evaluate(test_csv_path):
    with open(test_csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        questions = list(reader)

    hits = 0
    total = len(questions)

    for row in questions:
        question = row['question']
        expected_section = row['expected_section'].strip()
        expected_document = row['expected_document'].strip()

        results = retrieve(question, k=5)

        # Show what the model actually returned as top-1
        if results:
            top_doc, top_score = results[0]
            top_info = f"{top_doc.metadata['source']} Sec {top_doc.metadata['section_number']} (score {top_score:.4f})"
        else:
            top_info = "NO RESULTS / NOT_LEGAL"

        # Check for hit
        found = False
        if expected_section.upper() == "NOT_LEGAL":
            found = (len(results) == 0)
        else:
            for doc, score in results:
                if (doc.metadata['section_number'] == expected_section and
                    doc.metadata['source'] == expected_document):
                    found = True
                    break

        if found:
            hits += 1
            print(f"PASS | {question[:60]:<60} → {top_info}")
        else:
            print(f"FAIL | {question[:60]:<60} → {top_info}   (expected {expected_document} Sec {expected_section})")

    recall = hits / total if total > 0 else 0
    print(f"\n{'='*50}")
    print(f"Context Recall: {hits}/{total} = {recall:.2%}")
    print(f"Target: > 0.70 {'Pass' if recall >= 0.7 else 'Fail'}")

if __name__ == "__main__":
    evaluate("test_set/test_questions_4.csv")