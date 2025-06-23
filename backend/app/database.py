# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use SQLite for local dev
SQLALCHEMY_DATABASE_URL = "sqlite:///./feedback.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # required only for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔥 THIS is the Base you're importing
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()