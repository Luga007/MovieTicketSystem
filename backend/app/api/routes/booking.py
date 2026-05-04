from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.booking import Booking
from app.models.showtime import Showtime
from app.models.users import User

router = APIRouter(prefix="/bookings", tags=["Booking"])

# @router.post("/")
# def create_booking(user_id: int, showtime_id: int, db: Session = Depends(get_db)):
    
#     # проверка пользователя
#     user = db.query(User).filter(User.user_id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     # проверка сеанса
#     showtime = db.query(Showtime).filter(Showtime.showtime_id == showtime_id).first()
#     if not showtime:
#         raise HTTPException(status_code=404, detail="Showtime not found")

#     booking = Booking(
#         user_id=user_id,
#         showtime_id=showtime_id
#     )

#     db.add(booking)
#     db.commit()
#     db.refresh(booking)

#     return booking

@router.post("/bookings/")
def create_booking(
    user_id: int,
    showtime_id: int,
    seat_id: int,
    db: Session = Depends(get_db)
):
    booking = Booking(
        user_id=user_id,
        showtime_id=showtime_id,
        seat_id=seat_id,
        status="pending"
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking


@router.get("/")
def get_bookings(db: Session = Depends(get_db)):
    bookings = db.query(Booking).all()

    result = []
    for b in bookings:
        result.append({
            "booking_id": b.booking_id,
            "user": b.user.name,
            "movie": b.showtime.movie.title,
            "hall": b.showtime.hall.name,
            "time": b.showtime.start_time,
            "status": b.status
        })

    return result


@router.put("/{booking_id}")
def update_booking(
    booking_id: int,
    user_id: int,
    showtime_id: int,
    seat_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    booking.user_id = user_id
    booking.showtime_id = showtime_id
    booking.seat_id = seat_id
    booking.status = status  

    db.commit()
    db.refresh(booking)

    return booking


@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    db.delete(booking)
    db.commit()

    return {"message": "Booking deleted"}