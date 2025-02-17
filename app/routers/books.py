from fastapi import APIRouter, Depends, HTTPException, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .. import crud, models
from ..database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def check_session(request: Request):
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=403, detail="Not authenticated")


@router.get("/api/books-with-cities")
def read_books_with_cities(db: Session=Depends(get_db)):
    return crud.get_books_with_cities(db)


@router.get("/books", response_class=HTMLResponse)
def manage_books(request: Request, db: Session=Depends(get_db)):
    check_session(request)  # Protect the route
    books = (
        db.query(
            models.Book.id,
            models.Book.title,
            models.Book.author,
            models.User.username,
            models.City.city_name,
        )
        .select_from(models.Book)  # Tentukan tabel awal
        .join(models.User, models.Book.user_id == models.User.id)  # Join ke User
        .join(models.City, models.User.city_code == models.City.city_code)  # Join ke City
        .all()
    )  # Ambil semua buku dengan data pengguna dan kota

    print("Fetched books:", books)  # Debugging line

    return templates.TemplateResponse("manage_books.html", {"request": request, "books": books})


@router.get("/books/add", response_class=HTMLResponse)
def add_book(request: Request, db: Session=Depends(get_db)):
    check_session(request)  # Protect the route
    users = db.query(models.User).all()  # Fetch all users
    return templates.TemplateResponse("add_book.html", {"request": request, "users": users})


@router.post("/books")
def create_book(title: str=Form(...), author: str=Form(...), user_id: int=Form(...), db: Session=Depends(get_db)):
    new_book = models.Book(title=title, author=author, user_id=user_id)
    db.add(new_book)
    db.commit()
    # return {"message": "Book added successfully"}
    return RedirectResponse(url="/books", status_code=303)


@router.get("/books/edit/{book_id}", response_class=HTMLResponse)
def edit_book(book_id: int, request: Request, db: Session=Depends(get_db)):
    check_session(request)  # Protect the route
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    users = db.query(models.User).all()  # Fetch all users
    return templates.TemplateResponse("edit_book.html", {"request": request, "users": users, "book": book, "book_id": book_id})


@router.post("/books/edit/{book_id}")
def update_book(book_id: int, title: str=Form(...), author: str=Form(...), user_id: int=Form(...), db: Session=Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    print(book)
    if book:
        book.title = title
        book.author = author
        book.user_id = user_id
        db.commit()
        # return {"message": "Book updated successfully"}
        return RedirectResponse(url="/books/edit/" + str(book_id), status_code=303)
    
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session=Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return {"message": f"Book with ID {book_id} deleted."}
    raise HTTPException(status_code=404, detail="Book not found")
