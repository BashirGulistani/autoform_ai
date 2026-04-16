from typing import Dict, Any


def map_to_target_schema(extracted_data: Dict[str, Any], schema_name: str) -> Dict[str, Any]:
    """
    Maps extracted fields into a target schema.

    Example:
    full_name -> applicant_name
    date_of_birth -> dob
    passport_number -> document_id
    """
    schema_name = schema_name.lower()

    if schema_name == "visa_form":
        return {
            "applicant_name": extracted_data.get("full_name"),
            "dob": extracted_data.get("date_of_birth"),
            "document_id": extracted_data.get("passport_number"),
        }

    if schema_name == "job_application":
        return {
            "candidate_name": extracted_data.get("full_name"),
            "birth_date": extracted_data.get("date_of_birth"),
            "government_id": extracted_data.get("passport_number"),
        }

    return extracted_data
