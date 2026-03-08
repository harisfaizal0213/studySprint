#Import tools to define columns in the databse table
from sqlalchemy import Column, Integer, String, DateTime
#Imoprt SQL functions
from sqlalchemy.sql import func
'''Import database engine from db.py file.
Engine is the object SQLALchemy uses to connect to database
- Bridge between Python app and PostgreSQL
''' 
from app.db import engine
#Imports the function that creats the base class for the models
from sqlalchemy.orm import declarative_base

#Need this so that we can use Python to make Database tables
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id= Column(Integer, primary_key=True, index=True)
    email = Column(String, unique = True, index=True)
    password_hash = Column(String)
    #Creates a column that stores when the user was created
    created_at = Column(DateTime(timezone=True), server_default=func.now())
