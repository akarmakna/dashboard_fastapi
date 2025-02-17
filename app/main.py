from fastapi import FastAPI, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .database import engine, get_db
from . import models
from .routers import auth, books
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(books.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root():
    return RedirectResponse(url="/login")  # Redirect to login page
