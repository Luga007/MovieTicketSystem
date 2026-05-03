from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cinema(Base):
    __tablename__ = "cinemas"

    cinema_id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    halls = relationship("Hall", backref="cinema")