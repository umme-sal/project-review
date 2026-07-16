from pydantic import BaseModel


class TicketCreate(BaseModel):

    title: str

    description: str


class TicketUpdate(BaseModel):

    title: str | None = None

    description: str | None = None

    status: str | None = None

    category: str | None = None

    priority: str | None = None

    sentiment: str | None = None


class TicketResponse(BaseModel):

    id: int

    title: str

    description: str

    category: str | None

    priority: str | None

    sentiment: str | None

    status: str

    class Config:

        from_attributes = True