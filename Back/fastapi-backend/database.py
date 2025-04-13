import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("postgresql://todoapp_58p7_user:UuHOCqgYsIgAljSN2ZTuB4YIPzXQdbi5@dpg-cvtmpo24d50c73ak73s0-a/todoapp_58p7")  # Use full URL from Render

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
