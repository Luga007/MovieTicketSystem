from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.booking import Booking
from app.models.tickets import Ticket

router = APIRouter(prefix="/bookings", tags=["Booking"])

@router.post("/")
def create_booking(user_id: int, showtime_id: int, db: Session = Depends(get_db)):
    booking = Booking(user_id=user_id, showtime_id=showtime_id)
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

@router.post("/{booking_id}/tickets")
def add_ticket(booking_id: int, seat_id: int, price: float, db: Session = Depends(get_db)):
    ticket = Ticket(
        booking_id=booking_id,
        seat_id=seat_id,
        price=price
    )
    db.add(ticket)
    db.commit()
    return ticket