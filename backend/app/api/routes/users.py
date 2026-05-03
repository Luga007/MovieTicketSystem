from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.users import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(name: str, email: str, password: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()