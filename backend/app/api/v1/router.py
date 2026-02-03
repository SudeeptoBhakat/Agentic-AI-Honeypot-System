from fastapi import APIRouter
from .health import router as health_router
from .predict import router as predict_router
from .views import router as calls_router
api_router = APIRouter()

api_router.include_router(calls_router, prefix="/calls", tags=["Calls"])