from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///./dealerCars.db"

# Creates database engine config
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Creates database session with provided config
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db():
    """
    Get a database session
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
