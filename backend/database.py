from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:pass123@localhost:5432/jobscraperdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Dependency function for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()