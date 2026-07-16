from fastapi import APIRouter

from app.schemas.priority import (
    PriorityRequest,
    PriorityResponse
)

from app.services.priority_service import PriorityService

router = APIRouter(
    prefix="/priority",
    tags=["Priority Prediction"]
)


@router.post(
    "",
    response_model=PriorityResponse
)
def predict(request: PriorityRequest):

    return PriorityService.predict(
        request.text
    )