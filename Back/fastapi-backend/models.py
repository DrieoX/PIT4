from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
from datetime import datetime

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)
    deadline = Column(DateTime, default=datetime.utcnow)
