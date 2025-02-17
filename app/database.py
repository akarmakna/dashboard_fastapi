from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username@localhost/db_name"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root@localhost/library_2"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
