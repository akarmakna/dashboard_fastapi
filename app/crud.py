from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

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
        .select_from(models.Book)  # Pastikan titik awal query adalah Book
        .join(models.User, models.Book.user_id == models.User.id)
        .join(models.City, models.User.city_code == models.City.city_code)
        .all()
    )
