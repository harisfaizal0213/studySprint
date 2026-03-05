from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db import get_db 

app = FastAPI(title="StudySprint API")

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "studysprint-api"}

@app.get("/api/db-health")
def db_health(db: Session = Depends(get_db)):
    db.execute(text("Select 1"))
    return {"database": "connected"}
