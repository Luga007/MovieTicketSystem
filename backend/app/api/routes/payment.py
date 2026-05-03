from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.payment import Payment
from app.models.booking import Booking
from app.models.tickets import Ticket

router = APIRouter(prefix="/payments", tags=["Payment"])

@router.post("/pay/{booking_id}")
def pay_booking(
    booking_id: int,
    payment_method: str = "card",
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    if booking.status == "paid":
        raise HTTPException(status_code=400, detail="Already paid")

    if not booking.seat_id:
        raise HTTPException(status_code=400, detail="Seat not selected")

    showtime = booking.showtime
    amount = showtime.price

    # 1. create payment
    payment = Payment(
        booking_id=booking.booking_id,
        amount=amount,
        payment_method=payment_method,
        status="success"
    )

    # 2. mark booking paid
    booking.status = "paid"

    # 3. create ticket AFTER payment
    ticket = Ticket(
        booking_id=booking.booking_id,
        seat_id=booking.seat_id,
        price=amount
    )

    db.add(payment)
    db.add(ticket)
    db.commit()

    db.refresh(ticket)

    return {
        "message": "Payment successful",
        "booking_id": booking_id,
        "ticket_id": ticket.ticket_id,
        "amount": amount,
        "seat_id": booking.seat_id
    }