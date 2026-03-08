from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db import get_db, engine 
# Import Base object from model file
from app.models.user import Base

app = FastAPI(title="StudySprint API")

#IMPORTANT need this to connect the session to the dataabse
Base.metadata.create_all(bind=engine)

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "studysprint-api"}

@app.get("/api/db-health")
def db_health(db: Session = Depends(get_db)):
    db.execute(text("Select 1"))
    return {"database": "connected"}
