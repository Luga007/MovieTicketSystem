from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Hall(Base):
    __tablename__ = "halls"

    hall_id = Column(Integer, primary_key=True)
    cinema_id = Column(Integer, ForeignKey("cinemas.cinema_id"))
    name = Column(String)
    total_seats = Column(Integer)

    seats = relationship("Seat", backref="hall")