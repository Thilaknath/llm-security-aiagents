import os
import fitz  # PyMuPDF for PDF processing

def extract_text_from_pdf(pdf_file):
    """
    Extracts text content from an uploaded PDF file (Streamlit InMemoryUploadedFile).
    """
    text = ""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()
    return text

def load_best_practices(directory_path):
    """
    Load and process all best practice PDFs in the specified directory.
    Returns a dictionary with filenames as keys and extracted text as values.
    """
    best_practices = {}
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory_path, filename)
            with open(pdf_path, 'rb') as file:
                best_practices[filename] = extract_text_from_pdf(file)
    return best_practices

def summary_best_practices(practices_text):
    """
    Extracts section headers or main topics from best practices content for summary.
    This can be done by retrieving headers or keywords that indicate best practice areas.
    """
    # Assuming sections are organized with keywords like 'Section', 'Part', or similar
    summary = []
    lines = practices_text.split('\n')
    for line in lines:
        if "section" in line.lower() or "part" in line.lower():
            summary.append(line.strip())
    return "; ".join(summary) if summary else practices_text[:100] + "..."  # Limit if no sections

def extract_best_practices(parsed_content, best_practices):
    """
    Matches best practices based on keywords, returning a list of applicable document sections.
    """
    suggestions = []
    for doc_name, practices_text in best_practices.items():
        if any(keyword.lower() in parsed_content.lower() for keyword in practices_text.split()):
            section_summary = summary_best_practices(practices_text)
            suggestions.append((section_summary, doc_name))
    return suggestions