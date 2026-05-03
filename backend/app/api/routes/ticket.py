from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.tickets import Ticket

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.get("/")
def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()

    return [
        {
            "ticket_id": t.ticket_id,
            "booking_id": t.booking_id,
            "seat_id": t.seat_id,
            "price": t.price,
        }
        for t in tickets
    ]