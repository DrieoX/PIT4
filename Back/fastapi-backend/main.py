from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import todos  # Assuming you have a router for todo operations

app = FastAPI()

# Configure CORS to allow requests from your React frontend
origins = [
    "https://beautiful-gnome-a14487.netlify.app",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows only specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all standard methods
    allow_headers=["*"],  # Allows all headers
)

# Include your routers
app.include_router(todos.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to your To-Do List API"}
