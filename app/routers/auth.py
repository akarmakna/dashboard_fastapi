from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db
from passlib.context import CryptContext
from fastapi.templating import Jinja2Templates

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
templates = Jinja2Templates(directory="app/templates")

router = APIRouter()


@router.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
async def login(request: Request, db: Session=Depends(get_db)):
    form = await request.form()  # Await the form data
    username = form.get("username")
    password = form.get("password")
    user = crud.get_user(db, username=username)
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="user_id", value=str(user.id))  # Set user_id cookie
    response.set_cookie(key="user_name", value=str(user.username))  # Set user_id cookie
    return response


@router.get("/register")
def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
async def register(request: Request, db: Session=Depends(get_db)):
    form = await request.form()
    user = schemas.UserCreate(username=form.get("username"), password=form.get("password"))
    crud.create_user(db=db, user=user)
    return RedirectResponse(url="/login", status_code=303)  # Redirect to login page after registration


@router.get("/dashboard")
def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@router.get("/change-password")
def get_change_password(request: Request):
    return templates.TemplateResponse("change_password.html", {"request": request})


@router.post("/change-password")
async def change_password(request: Request, db: Session=Depends(get_db)):
    form = await request.form()  # Await the form data
    current_password = form.get("current_password")
    new_password = form.get("new_password")
    user_name = request.cookies.get("user_name")  # Get user name from cookie
    user = crud.get_user(db, username=user_name)  # Assuming user_name is the username for simplicity
    if not user or not pwd_context.verify(current_password, user.password):
        raise HTTPException(status_code=400, detail="Invalid current password")
    
    # Update the user's password
    user.password = pwd_context.hash(new_password)
    db.commit()
    return RedirectResponse(url="/dashboard", status_code=303)  # Redirect to dashboard after changing password


@router.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("user_id")  # Clear the user_id cookie
    response.delete_cookie("user_name")  # Clear the user_name cookie
    return response


@router.get("/users", response_model=list[schemas.User])
def read_users(db: Session=Depends(get_db)):
    return db.query(models.User).all()
