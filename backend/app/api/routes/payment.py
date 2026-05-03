from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.payment import Payment

router = APIRouter(prefix="/payments", tags=["Payment"])

@router.post("/")
def create_payment(booking_id: int, amount: float, method: str, db: Session = Depends(get_db)):
    payment = Payment(
        booking_id=booking_id,
        amount=amount,
        payment_method=method,
        status="paid"
    )
    db.add(payment)
    db.commit()
    return payment