from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from sqlalchemy.orm import declarative_base
from routers import todos  # Assuming you have a router for todo operations

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS to allow requests from your React frontend
origins = [
    "https://beautiful-gnome-a14487.netlify.app/",  # Replace with your deployed frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers
app.include_router(todos.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to your To-Do List API"}


