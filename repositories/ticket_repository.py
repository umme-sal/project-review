from sqlalchemy.orm import Session
from app.models.ticket import Ticket


class TicketRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, ticket_data: dict):

        ticket = Ticket(**ticket_data)

        self.db.add(ticket)

        self.db.commit()

        self.db.refresh(ticket)

        return ticket

    def get_all(self):

        return self.db.query(Ticket).all()

    def get_by_id(self, ticket_id: int):

        return (
            self.db.query(Ticket)
            .filter(Ticket.id == ticket_id)
            .first()
        )

    def update(self, ticket_id: int, data: dict):

        ticket = self.get_by_id(ticket_id)

        if ticket is None:
            return None

        for key, value in data.items():
            setattr(ticket, key, value)

        self.db.commit()

        self.db.refresh(ticket)

        return ticket

    def delete(self, ticket_id: int):

        ticket = self.get_by_id(ticket_id)

        if ticket is None:
            return False

        self.db.delete(ticket)

        self.db.commit()

        return True