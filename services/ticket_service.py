from sqlalchemy.orm import Session

from app.repositories.ticket_repository import TicketRepository


class TicketService:

    def __init__(self, db: Session):

        self.repository = TicketRepository(db)

    def create_ticket(self, ticket):

        return self.repository.create(
            ticket.model_dump()
        )

    def get_all_tickets(self):

        return self.repository.get_all()

    def get_ticket(self, ticket_id: int):

        return self.repository.get_by_id(ticket_id)

    def update_ticket(self, ticket_id: int, ticket):

        return self.repository.update(
            ticket_id,
            ticket.model_dump(exclude_unset=True)
        )

    def delete_ticket(self, ticket_id: int):

        return self.repository.delete(ticket_id)