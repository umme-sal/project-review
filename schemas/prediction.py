from pydantic import BaseModel


class PredictionRequest(BaseModel):

    text: str


class PredictionResponse(BaseModel):

    category: str

    confidence: float