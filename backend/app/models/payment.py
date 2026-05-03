from sqlalchemy import Column, Integer, Float, ForeignKey, String, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey("bookings.booking_id"))

    amount = Column(Integer)
    payment_method = Column(String)
    status = Column(String, default="pending")

    paid_at = Column(TIMESTAMP, server_default=func.now())