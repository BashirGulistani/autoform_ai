from __future__ import annotations

import os
import shutil
import uuid
from pathlib import Path
from typing import BinaryIO, Optional

from app.core.config import settings


class FileManager:
    """
    Handles upload storage, output storage, temp file cleanup,
    and safe path creation for the AutoForm AI project.
    """

    def __init__(self, upload_dir: Optional[str] = None, output_dir: Optional[str] = None) -> None:
        self.upload_dir = Path(upload_dir or settings.upload_dir)
        self.output_dir = Path(output_dir or settings.output_dir)
        self.temp_dir = self.upload_dir / "temp"

        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)


    def generate_safe_filename(self, original_filename: str) -> str:
        """
        Convert the original filename into a unique safe filename.
        """
        ext = Path(original_filename).suffix.lower()
        stem = Path(original_filename).stem.strip().replace(" ", "_")
        stem = "".join(ch for ch in stem if ch.isalnum() or ch in ("_", "-"))

        if not stem:
            stem = "document"

        return f"{stem}_{uuid.uuid4().hex[:10]}{ext}"

    def save_upload_bytes(self, file_bytes: bytes, original_filename: str) -> str:
        """
        Save uploaded bytes to disk and return the file path.
        """
        safe_filename = self.generate_safe_filename(original_filename)
        file_path = self.upload_dir / safe_filename

        with open(file_path, "wb") as f:
            f.write(file_bytes)

        return str(file_path)


    def save_upload_stream(self, file_stream: BinaryIO, original_filename: str) -> str:
        """
        Save uploaded binary stream to disk and return path.
        """
        safe_filename = self.generate_safe_filename(original_filename)
        file_path = self.upload_dir / safe_filename

        with open(file_path, "wb") as out_file:
            shutil.copyfileobj(file_stream, out_file)

        return str(file_path)

    def save_text_output(self, text: str, output_name: str) -> str:
        """
        Save extracted or processed text output.
        """
        safe_name = self.generate_safe_filename(output_name).rsplit(".", 1)[0] + ".txt"
        file_path = self.output_dir / safe_name

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

        return str(file_path)





