from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True  # Updated to the new key

class BookCreate(BaseModel):
    title: str
    author: str

class Book(BookCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True  # Updated to the new key
