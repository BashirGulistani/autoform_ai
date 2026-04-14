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
    extracted_text = extract_text_from_document(file_bytes=file_bytes, filename=filename)
    structured_data = extract_structured_data(extracted_text)
    missing_fields = detect_missing_fields(structured_data)

    return {
        "filename": filename,
        "extracted_text": extracted_text,
        "structured_data": structured_data,
        "missing_fields": missing_fields,
    }
