import os
import uuid
from datetime import datetime
from fastapi import UploadFile

AUDIO_DIR = "app/storage/audio"

os.makedirs(AUDIO_DIR, exist_ok=True)

def save_audio_file(file: UploadFile) -> str:
    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}_{datetime.utcnow().timestamp()}.{ext}"

    file_path = os.path.join(AUDIO_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path
