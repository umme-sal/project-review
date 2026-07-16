from fastapi import APIRouter

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse
)

from app.services.prediction_service import (
    PredictionService
)

router = APIRouter(

    prefix="/predict",

    tags=["AI Prediction"]

)

service = PredictionService()


@router.post(
    "",
    response_model=PredictionResponse
)
def predict(request: PredictionRequest):

    return service.predict(request.text)