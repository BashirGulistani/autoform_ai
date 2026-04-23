from __future__ import annotations

from pathlib import Path
from typing import Iterable


ALLOWED_EXTENSIONS = {
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".tiff",
    ".bmp",
    ".txt",
}



DEFAULT_MAX_FILE_SIZE_MB = 20


class DocumentValidationError(Exception):
    """Raised when an uploaded document fails validation."""


def validate_file_extension(filename: str, allowed_extensions: Iterable[str] = ALLOWED_EXTENSIONS) -> None:
    """
    Ensure the uploaded file has an allowed extension.
    """
    suffix = Path(filename).suffix.lower()

    if suffix not in allowed_extensions:
        raise DocumentValidationError(
            f"Unsupported file type: {suffix or 'unknown'}. "
            f"Allowed types are: {', '.join(sorted(allowed_extensions))}"
        )

def validate_file_size(file_bytes: bytes, max_file_size_mb: int = DEFAULT_MAX_FILE_SIZE_MB) -> None:
    """
    Ensure the uploaded file size does not exceed the configured max.
    """
    size_bytes = len(file_bytes)
    max_bytes = max_file_size_mb * 1024 * 1024

    if size_bytes > max_bytes:
        raise DocumentValidationError(
            f"File is too large. Max allowed size is {max_file_size_mb} MB."
        )


def validate_non_empty(file_bytes: bytes) -> None:
    """
    Ensure uploaded content is not empty.
    """
    if not file_bytes:
        raise DocumentValidationError("Uploaded file is empty.")


def validate_filename(filename: str) -> None:
    """
    Ensure the filename exists and is not suspiciously malformed.
    """
    if not filename or not filename.strip():
        raise DocumentValidationError("Filename is missing.")



    stripped = filename.strip()

    if len(stripped) > 255:
        raise DocumentValidationError("Filename is too long.")

    illegal_chars = {"\x00", "\n", "\r"}
    if any(ch in stripped for ch in illegal_chars):
        raise DocumentValidationError("Filename contains invalid characters.")












