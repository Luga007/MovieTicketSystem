from fastapi import FastAPI

from app.api.routes import users, cinema, movies, booking, payment

app = FastAPI()

app.include_router(users.router)
app.include_router(cinema.router)
app.include_router(movies.router)
app.include_router(booking.router)
app.include_router(payment.router)