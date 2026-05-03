from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.cinema import Cinema
from app.models.hall import Hall
from app.models.seats import Seat

router = APIRouter(prefix="/cinemas", tags=["Cinema"])



@router.post("/")
def create_cinema(name: str, location: str, db: Session = Depends(get_db)):
    cinema = Cinema(name=name, location=location)
    db.add(cinema)
    db.commit()
    db.refresh(cinema)
    return cinema



@router.get("/")
def get_cinemas(db: Session = Depends(get_db)):
    return db.query(Cinema).all()



@router.get("/{cinema_id}")
def get_cinema(cinema_id: int, db: Session = Depends(get_db)):
    cinema = db.query(Cinema).filter(Cinema.cinema_id == cinema_id).first()
    if not cinema:
        return {"error": "Cinema not found"}
    return cinema



@router.post("/{cinema_id}/halls")
def create_hall(cinema_id: int, name: str, total_seats: int, db: Session = Depends(get_db)):
    hall = Hall(cinema_id=cinema_id, name=name, total_seats=total_seats)
    db.add(hall)
    db.commit()
    db.refresh(hall)
    return hall



@router.get("/{cinema_id}/halls")
def get_halls(cinema_id: int, db: Session = Depends(get_db)):
    return db.query(Hall).filter(Hall.cinema_id == cinema_id).all()


@router.get("/halls/{hall_id}")
def get_hall(hall_id: int, db: Session = Depends(get_db)):
    hall = db.query(Hall).filter(Hall.hall_id == hall_id).first()
    if not hall:
        return {"error": "Hall not found"}
    return hall


@router.post("/halls/{hall_id}/seats")
def create_seat(hall_id: int, row: str, number: int, seat_type: str, db: Session = Depends(get_db)):
    seat = Seat(hall_id=hall_id, row=row, number=number, seat_type=seat_type)
    db.add(seat)
    db.commit()
    db.refresh(seat)
    return seat