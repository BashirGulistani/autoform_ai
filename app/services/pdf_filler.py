import json
from pathlib import Path
from typing import Dict, Any

from app.core.config import settings


def fill_pdf_placeholder(template_name: str, data: Dict[str, Any]) -> str:
    """
    Starter placeholder for PDF filling.

    For now, it writes mapped data to a JSON file
    that simulates a filled form output.
    Later replace with real PDF form filling.
    """
