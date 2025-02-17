from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)  # Specify length for VARCHAR
    password = Column(String)
    city_code = Column(String(10), ForeignKey('cities.city_code'))  # Add city_code field
    books = relationship("Book", back_populates="user")  # Define relationship
    city = relationship("City")  # Relationship to City

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key reference
    user = relationship("User", back_populates="books")  # Define relationship

class City(Base):
    __tablename__ = "cities"

    city_code = Column(String(10), primary_key=True)
    city_name = Column(String(100))
    latitude = Column(Integer)
    longitude = Column(Integer)
