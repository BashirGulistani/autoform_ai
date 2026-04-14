from pydantic import BaseModel, Field
from typing import Any, Dict, List


class HealthResponse(BaseModel):
    status: str


class ExtractResponse(BaseModel):
    filename: str
    extracted_text: str
    structured_data: Dict[str, Any] = Field(default_factory=dict)
    missing_fields: List[str] = Field(default_factory=list)
