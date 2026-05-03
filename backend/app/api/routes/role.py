from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.role import Role
from app.schemas.role import RoleCreate, RoleOut

router = APIRouter(prefix="/roles", tags=["Roles"])


@router.post("/", response_model=RoleOut)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    if db.query(Role).filter(Role.name == role.name).first():
        raise HTTPException(400, "Role exists")

    r = Role(name=role.name)
    db.add(r)
    db.commit()
    db.refresh(r)
    return r


@router.get("/", response_model=list[RoleOut])
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()


@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).get(role_id)
    if not role:
        raise HTTPException(404, "Not found")

    db.delete(role)
    db.commit()
    return {"message": "deleted"}