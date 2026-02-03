from app.ml.loader import ModelLoader
import logging

logger = logging.getLogger(__name__)

def predict(data: list):
    try:
        model = ModelLoader.load_model()
        # Ensure data is reshaped if necessary or validated
        result = model.predict([data])
        return result.tolist()
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}", exc_info=True)
        raise e