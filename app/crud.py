from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate, city_code: str):
    db_user = models.User(username=user.username, password=pwd_context.hash(user.password), city_code=city_code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_cities(db: Session):
    return db.query(models.City).all()  # Fetch all cities

def get_books_with_cities(db: Session):
    results = (
        db.query(models.Book, models.User, models.City)
        .select_from(models.Book)
        .join(models.User, models.Book.user_id == models.User.id)
        .join(models.City, models.User.city_code == models.City.city_code)
        .all()
    )
    
    # Log the results for debugging
    print("Results fetched:", results)

    # Transform results into a serializable format
    return [
        {
            "book": book.title,
            "author": user.username,
            "city": {
                "city_name": city.city_name,
                "latitude": city.latitude,
                "longitude": city.longitude
            }
        }
        for book, user, city in results
    ]

def get_books_with_cities_before(db: Session):
    return (
        db.query(models.Book, models.User, models.City)
        .select_from(models.Book)  # Ensure the starting point of the query is Book
        .join(models.User, models.Book.user_id == models.User.id)
        .join(models.City, models.User.city_code == models.City.city_code)
        .all()
    )
