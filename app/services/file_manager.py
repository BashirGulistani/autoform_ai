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







