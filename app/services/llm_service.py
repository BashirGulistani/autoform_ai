import re
from typing import Dict, Any


def extract_structured_data(text: str) -> Dict[str, Any]:
    """
    Starter mock extraction logic.

    Replace later with:
    - Ollama
    - OpenAI
    - Haystack pipeline
    """
    data: Dict[str, Any] = {
        "full_name": None,
        "date_of_birth": None,
        "passport_number": None,
    }

    name_match = re.search(r"Name:\s*(.+)", text, re.IGNORECASE)
    dob_match = re.search(r"Date of Birth:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", text, re.IGNORECASE)
    passport_match = re.search(r"Passport Number:\s*([A-Za-z0-9]+)", text, re.IGNORECASE)

    if name_match:
        data["full_name"] = name_match.group(1).strip()

    if dob_match:
        data["date_of_birth"] = dob_match.group(1).strip()

    if passport_match:
        data["passport_number"] = passport_match.group(1).strip()

    return data
