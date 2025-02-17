from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware  # Correct import
from .routers import auth, books

app = FastAPI()

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

# Include routers
app.include_router(auth.router)
app.include_router(books.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
