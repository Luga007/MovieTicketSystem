from pydantic import BaseModel
from typing import List

class BookingCreate(BaseModel):
    showtime_id: int
    seat_ids: List[int]

class BookingResponse(BaseModel):
    booking_id: int
    status: str

    class Config:
        from_attributes = True