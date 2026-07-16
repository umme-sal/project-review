from fastapi import APIRouter

from app.schemas.sentiment import (
    SentimentRequest,
    SentimentResponse
)

from app.services.sentiment_service import (
    SentimentService
)

router = APIRouter(

    prefix="/sentiment",

    tags=["Sentiment Analysis"]

)

service = SentimentService()


@router.post(
    "",
    response_model=SentimentResponse
)
def analyze_sentiment(request: SentimentRequest):

    return service.predict(request.text)