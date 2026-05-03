from fastapi import FastAPI

from app.api.routes import users, cinema, movies, booking, payment
from app.db.session import engine
from app.db.base import Base


from app.models import cinema, users, role, movies, booking, payment

app = FastAPI()

app.include_router(users.router)
app.include_router(cinema.router)
app.include_router(movies.router)
app.include_router(booking.router)
app.include_router(payment.router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)