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

