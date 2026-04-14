from typing import Optional


def extract_text_from_document(file_bytes: bytes, filename: str) -> str:
    """
    Starter OCR/text extraction service.

    Later you can replace this with:
    - Tesseract
    - PaddleOCR
    - AWS Textract
    - Azure Document Intelligence
    """
    if not file_bytes:
        return ""

    lower_name = filename.lower()

    if lower_name.endswith(".txt"):
        try:
            return file_bytes.decode("utf-8")
        except UnicodeDecodeError:
            return file_bytes.decode("latin-1", errors="ignore")

    # Placeholder behavior for PDFs/images until OCR is integrated.
    return (
        f"Mock extracted text from file: {filename}\n"
        "Name: John Doe\n"
        "Date of Birth: 1995-01-01\n"
        "Passport Number: A12345678\n"
    )
