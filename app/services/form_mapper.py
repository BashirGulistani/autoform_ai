from typing import Dict, Any


def map_to_target_schema(extracted_data: Dict[str, Any], schema_name: str) -> Dict[str, Any]:
    """
    Maps extracted fields into a target schema.

    Example:
    full_name -> applicant_name
    date_of_birth -> dob
    passport_number -> document_id
    """
