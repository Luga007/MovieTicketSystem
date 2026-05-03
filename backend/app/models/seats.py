from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Seat(Base):
    __tablename__ = "seats"

    seat_id = Column(Integer, primary_key=True)
    hall_id = Column(Integer, ForeignKey("halls.hall_id"))

    row = Column(String)
    number = Column(Integer)
    seat_type = Column(String)