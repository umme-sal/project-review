from fastapi import APIRouter

from app.schemas.summary import (
    SummaryRequest,
    SummaryResponse
)

from app.services.summary_service import SummaryService

router = APIRouter(

    prefix="/summary",

    tags=["Ticket Summary"]

)

service = SummaryService()


@router.post(
    "",
    response_model=SummaryResponse
)
def summarize(request: SummaryRequest):

    return service.summarize(
        request.text
    )