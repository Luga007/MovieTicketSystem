from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.movies import Movie
from app.models.showtime import Showtime
from datetime import datetime


router = APIRouter(prefix="/showtime", tags=["Showtime"])


@router.post("/showtime")
def create_showtime(
    movie_id: int,
    hall_id: int,
    start_time: datetime,
    price: float,
    db: Session = Depends(get_db)
):
    showtime = Showtime(
        movie_id=movie_id,
        hall_id=hall_id,
        start_time=start_time,
        price=price
    )
    db.add(showtime)
    db.commit()
    db.refresh(showtime)
    return showtime



@router.get("/showtime")
def get_showtimes(db: Session = Depends(get_db)):
    return db.query(Showtime).all()


@router.put("/showtime/{showtime_id}")
def update_showtime(
    showtime_id: int,
    movie_id: int,
    hall_id: int,
    start_time: datetime,
    price: float,
    db: Session = Depends(get_db)
):
    showtime = db.query(Showtime).filter(Showtime.showtime_id == showtime_id).first()

    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    showtime.movie_id = movie_id
    showtime.hall_id = hall_id
    showtime.start_time = start_time
    showtime.price = price

    db.commit()
    db.refresh(showtime)
    return showtime


@router.delete("/showtime/{showtime_id}")
def delete_showtime(showtime_id: int, db: Session = Depends(get_db)):
    showtime = db.query(Showtime).filter(Showtime.showtime_id == showtime_id).first()

    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")

    db.delete(showtime)
    db.commit()
    return {"message": "Showtime deleted"}