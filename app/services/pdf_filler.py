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
    output_dir = Path(settings.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{template_name}_filled.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return str(output_path)
