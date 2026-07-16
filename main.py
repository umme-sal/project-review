from fastapi import FastAPI
from app.models.user import User
from app.database.database import Base
from app.database.database import engine

from app.models.ticket import Ticket

from app.api.health import router as health_router
from app.api.ticket import router as ticket_router

from app.api.auth import router as auth_router
from app.api.prediction import (
    router as prediction_router
)
from app.api.duplicate import router as duplicate_router

from app.api.sentiment import router as sentiment_router
from app.api.summary import router as summary_router
from app.api.priority import router as priority_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise AI Support Intelligence Platform",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(ticket_router)
app.include_router(auth_router)
app.include_router(prediction_router)
app.include_router(sentiment_router)
app.include_router(duplicate_router)
app.include_router(summary_router)
app.include_router(priority_router)

@app.get("/")
def home():

    return {

        "message": "Enterprise AI Support Intelligence Platform"

    }