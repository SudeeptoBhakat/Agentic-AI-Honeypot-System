import joblib
from app.core.config import settings

class ModelLoader:
    _model = None

    @classmethod
    def load_model(cls):
        if cls._model is None:
            cls._model = joblib.load(settings.MODEL_PATH)
        return cls._model
