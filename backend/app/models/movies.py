from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship
from app.db.base import Base

class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    duration = Column(Integer)
    release_date = Column(Date)
    rating = Column(Float)

    showtimes = relationship("Showtime", backref="movie")