from app.services.ocr_service import extract_text_from_document
from app.services.llm_service import extract_structured_data
from app.utils.helpers import detect_missing_fields


def process_document_pipeline(file_bytes: bytes, filename: str) -> dict:
    """
    End-to-end processing:
    1. OCR / text extraction
    2. LLM-based structured extraction
    3. Missing field detection
    """
