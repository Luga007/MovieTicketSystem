from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.cinema import Cinema

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
        raise HTTPException(status_code=404, detail="Cinema not found")
    return cinema


@router.put("/{cinema_id}")
def update_cinema(cinema_id: int, name: str, location: str, db: Session = Depends(get_db)):
    cinema = db.query(Cinema).filter(Cinema.cinema_id == cinema_id).first()
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")

    cinema.name = name
    cinema.location = location
    db.commit()
    db.refresh(cinema)
    return cinema


@router.delete("/{cinema_id}")
def delete_cinema(cinema_id: int, db: Session = Depends(get_db)):
    cinema = db.query(Cinema).filter(Cinema.cinema_id == cinema_id).first()
    if not cinema:
        raise HTTPException(status_code=404, detail="Cinema not found")

    db.delete(cinema)
    db.commit()
    return {"message": "Cinema deleted"}