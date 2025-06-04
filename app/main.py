from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import auth, notes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes App")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])
