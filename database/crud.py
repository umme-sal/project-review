from sqlalchemy.orm import Session
from app.models.ticket import Ticket


def create_ticket(db: Session, ticket_data: dict):

    ticket = Ticket(**ticket_data)

    db.add(ticket)

    db.commit()

    db.refresh(ticket)

    return ticket


def get_all_tickets(db: Session):

    return db.query(Ticket).all()


def get_ticket(db: Session, ticket_id: int):

    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def update_ticket(db: Session, ticket_id: int, data: dict):

    ticket = get_ticket(db, ticket_id)

    if not ticket:
        return None

    for key, value in data.items():
        setattr(ticket, key, value)

    db.commit()

    db.refresh(ticket)

    return ticket


def delete_ticket(db: Session, ticket_id: int):

    ticket = get_ticket(db, ticket_id)

    if not ticket:
        return False

    db.delete(ticket)

    db.commit()

    return True