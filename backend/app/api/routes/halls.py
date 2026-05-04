from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.hall import Hall

router = APIRouter(prefix="/halls", tags=["Hall"])


@router.post("/")
def create_hall(cinema_id: int, name: str, total_seats: int, db: Session = Depends(get_db)):
    hall = Hall(cinema_id=cinema_id, name=name, total_seats=total_seats)
    db.add(hall)
    db.commit()
    db.refresh(hall)
    return hall


@router.get("/")
def get_halls(db: Session = Depends(get_db)):
    return db.query(Hall).all()


@router.get("/{hall_id}")
def get_hall(hall_id: int, db: Session = Depends(get_db)):
    hall = db.query(Hall).filter(Hall.hall_id == hall_id).first()
    if not hall:
        raise HTTPException(status_code=404, detail="Hall not found")
    return hall


@router.put("/{hall_id}")
def update_hall(hall_id: int, name: str, total_seats: int, db: Session = Depends(get_db)):
    hall = db.query(Hall).filter(Hall.hall_id == hall_id).first()
    if not hall:
        raise HTTPException(status_code=404, detail="Hall not found")

    hall.name = name
    hall.total_seats = total_seats
    db.commit()
    db.refresh(hall)
    return hall


@router.delete("/{hall_id}")
def delete_hall(hall_id: int, db: Session = Depends(get_db)):
    hall = db.query(Hall).filter(Hall.hall_id == hall_id).first()
    if not hall:
        raise HTTPException(status_code=404, detail="Hall not found")

    db.delete(hall)
    db.commit()
    return {"message": "Hall deleted"}

