from pydantic import BaseModel
import os


class Settings(BaseModel):
    app_name: str = "AutoForm AI"
    upload_dir: str = os.getenv("UPLOAD_DIR", "uploads")
    output_dir: str = os.getenv("OUTPUT_DIR", "outputs")
    llm_provider: str = os.getenv("LLM_PROVIDER", "mock")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3")
    max_file_size_mb: int = int(os.getenv("MAX_FILE_SIZE_MB", "20"))


settings = Settings()
