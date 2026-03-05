import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Example: postgresql+psycopg://user:pass@localhost:5432/dbname
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://studysprint:studysprintpass@localhost:5432/studysprint_db",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

        