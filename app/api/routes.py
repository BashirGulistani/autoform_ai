from fastapi import APIRouter, File, UploadFile, HTTPException

from app.schemas.response_models import ExtractResponse, HealthResponse
from app.services.pipeline import process_document_pipeline

router = APIRouter()




@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok")


@router.post("/extract", response_model=ExtractResponse)
async def extract_document(file: UploadFile = File(...)) -> ExtractResponse:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Invalid file upload")

    content = await file.read()
    result = process_document_pipeline(
        file_bytes=content,
        filename=file.filename,
    )
    return ExtractResponse(**result)
