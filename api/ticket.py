from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.ticket import TicketCreate
from app.schemas.ticket import TicketUpdate

from app.services import ticket_service

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/")
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):

    service = ticket_service.TicketService(db)

    return service.create_ticket(ticket)

@router.get("/")
def get_all_tickets(
    db: Session = Depends(get_db)
):

    service = ticket_service.TicketService(db)

    return service.get_all_tickets()


@router.get("/{ticket_id}")
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    ticket = ticket_service.get_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: int,
    ticket: TicketUpdate,
    db: Session = Depends(get_db)
):

    updated = ticket_service.update_ticket(
        db,
        ticket_id,
        ticket
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return updated


@router.delete("/{ticket_id}")
def delete_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    deleted = ticket_service.delete_ticket(
        db,
        ticket_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {

        "message": "Ticket deleted successfully"

    }