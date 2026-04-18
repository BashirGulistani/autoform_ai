from typing import Dict, Any, List


REQUIRED_FIELDS = [
    "full_name",
    "date_of_birth",
    "passport_number",
]


def detect_missing_fields(data: Dict[str, Any]) -> List[str]:
    missing = []
    for field in REQUIRED_FIELDS:
        value = data.get(field)
        if value is None or str(value).strip() == "":
            missing.append(field)
    return missing
