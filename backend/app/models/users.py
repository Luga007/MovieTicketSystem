from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    number = Column(String)

    role_id = Column(Integer, ForeignKey("roles.role_id"))
    created_at = Column(TIMESTAMP, server_default=func.now())

    role = relationship("Role")
    bookings = relationship("Booking", back_populates="user")