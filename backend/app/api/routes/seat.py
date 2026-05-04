from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.seats import Seat

router = APIRouter(prefix="/seats", tags=["Seat"])


@router.post("/")
def create_seat(hall_id: int, row: str, number: int, seat_type: str, db: Session = Depends(get_db)):
    seat = Seat(hall_id=hall_id, row=row, number=number, seat_type=seat_type)
    db.add(seat)
    db.commit()
    db.refresh(seat)
    return seat


@router.get("/")
def get_seats(db: Session = Depends(get_db)):
    return db.query(Seat).all()


@router.get("/{seat_id}")
def get_seat(seat_id: int, db: Session = Depends(get_db)):
    seat = db.query(Seat).filter(Seat.seat_id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")
    return seat


@router.put("/{seat_id}")
def update_seat(seat_id: int, row: str, number: int, seat_type: str, db: Session = Depends(get_db)):
    seat = db.query(Seat).filter(Seat.seat_id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")

    seat.row = row
    seat.number = number
    seat.seat_type = seat_type
    db.commit()
    db.refresh(seat)
    return seat


@router.delete("/{seat_id}")
def delete_seat(seat_id: int, db: Session = Depends(get_db)):
    seat = db.query(Seat).filter(Seat.seat_id == seat_id).first()
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")

    db.delete(seat)
    db.commit()
    return {"message": "Seat deleted"}