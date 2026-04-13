from fastapi import APIRouter, File, UploadFile, HTTPException

from app.schemas.response_models import ExtractResponse, HealthResponse
from app.services.pipeline import process_document_pipeline

router = APIRouter()




