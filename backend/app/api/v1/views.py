import uuid
from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import Call
from app.services.file_service import save_audio_file

router = APIRouter(prefix="", tags=["Calls"])

@router.post("/upload")
def upload_call_audio(
    audio_file: UploadFile = File(...),
    scammer_phone: str = Form(...),
    target_phone: str = Form(...),
    call_source: str = Form(...),
    db: Session = Depends(get_db)
):
    audio_path = save_audio_file(audio_file)

    call = Call(
        call_id=str(uuid.uuid4()),
        scammer_phone=scammer_phone,
        target_phone=target_phone,
        call_source=call_source,
        audio_file_path=audio_path,
        call_status="uploaded"
    )

    db.add(call)
    db.commit()
    db.refresh(call)

    return {
        "message": "Audio uploaded successfully",
        "call_id": call.call_id,
        "audio_path": audio_path
    }
