from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.movies import Movie
from app.models.showtime import Showtime
from datetime import datetime

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



@router.put("/{movie_id}")
def update_movie(movie_id: int, title: str, duration: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.movie_id == movie_id).first()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    movie.title = title
    movie.duration = duration

    db.commit()
    db.refresh(movie)
    return movie




@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.movie_id == movie_id).first()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    db.delete(movie)
    db.commit()
    return {"message": "Movie deleted"}