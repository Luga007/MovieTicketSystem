from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.movies import Movie
from app.models.showtime import Showtime

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/")
def create_movie(title: str, duration: int, db: Session = Depends(get_db)):
    movie = Movie(title=title, duration=duration)
    db.add(movie)
    db.commit()
    return movie

@router.get("/")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()

@router.post("/showtime")
def create_showtime(movie_id: int, hall_id: int, start_time: str, price: float, db: Session = Depends(get_db)):
    showtime = Showtime(
        movie_id=movie_id,
        hall_id=hall_id,
        start_time=start_time,
        price=price
    )
    db.add(showtime)
    db.commit()
    return showtime