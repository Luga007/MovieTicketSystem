from sqlalchemy import Column, Integer, ForeignKey, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey("bookings.booking_id"))
    seat_id = Column(Integer, ForeignKey("seats.seat_id"))

    price = Column(Float)

    booking = relationship("Booking", back_populates="tickets")

    __table_args__ = (
        UniqueConstraint("seat_id", "booking_id", name="unique_ticket"),
    )
    
seat = relationship("Seat")