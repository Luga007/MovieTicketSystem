from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    showtime_id = Column(Integer, ForeignKey("showtimes.showtime_id"))
    seat_id = Column(Integer, ForeignKey("seats.seat_id"))
    seat = relationship("Seat")

    showtime = relationship("Showtime")

    booking_time = Column(TIMESTAMP, server_default=func.now())
    status = Column(String, default="pending")

    user = relationship("User", back_populates="bookings")
    tickets = relationship("Ticket", back_populates="booking")

