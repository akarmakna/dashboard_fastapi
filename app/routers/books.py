from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/api/books-with-cities")
def read_books_with_cities(db: Session = Depends(get_db)):
    return crud.get_books_with_cities(db)

@router.get("/books")
def manage_books(request: Request, db: Session = Depends(get_db)):
    books_with_cities = crud.get_books_with_cities_before(db)  # Use the correct function
    return templates.TemplateResponse("manage_books.html", {"request": request, "books_with_cities": books_with_cities})

