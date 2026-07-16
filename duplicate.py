from fastapi import APIRouter

from pydantic import BaseModel

from app.services.duplicate_service import DuplicateService

router = APIRouter(
    prefix="/duplicate",
    tags=["Duplicate Detection"]
)


class DuplicateRequest(BaseModel):

    text: str


service = DuplicateService()


@router.post("")
def duplicate(request: DuplicateRequest):

    return service.search(
        request.text
    )