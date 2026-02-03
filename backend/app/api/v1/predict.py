from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import predict

router = APIRouter()

class PredictRequest(BaseModel):
    features: list[float]

@router.post("/predict")
def run_prediction(req: PredictRequest):
    return {"prediction": predict(req.features)}
