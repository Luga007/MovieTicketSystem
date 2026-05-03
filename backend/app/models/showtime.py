from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, Float
from app.db.base import Base

class Showtime(Base):
    __tablename__ = "showtimes"

    showtime_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.movie_id"))
    hall_id = Column(Integer, ForeignKey("halls.hall_id"))

    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    price = Column(Float)