# schemas.py
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoOut(TodoBase):
    id: int

    class Config:
        orm_mode = True
