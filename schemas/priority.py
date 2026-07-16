from pydantic import BaseModel

class PriorityRequest(BaseModel):
    text: str


class PriorityResponse(BaseModel):
    priority: str