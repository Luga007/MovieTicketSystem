from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.users import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(name: str, email: str, password: str, role: str = "user", db: Session = Depends(get_db)):
    user = User(
        name=name,
        email=email,
        password=password,
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.put("/{user_id}")
def update_user(user_id: int, name:str, email: str, password: str, number: str, role: str, db: Session = Depends(get_db) ):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = name
    user.email = email
    user.password = password
    user.number = number
    user.role = role

    db.commit()
    db.refresh(user)

    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}

