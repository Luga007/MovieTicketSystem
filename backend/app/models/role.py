from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)