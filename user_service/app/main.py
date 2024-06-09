from fastapi import FastAPI, Depends, HTTPException, status
from contextlib import asynccontextmanager
from app.db import create_db_and_tables



# Async context manager for application lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    # create_db_and_tables()  # Create database tables
    yield  # Application startup

# Create FastAPI app with custom lifespan and metadata
app = FastAPI(
    lifespan=lifespan,
    title="User_service_API",
    version="0.0.1",
    servers=[
        {
            "url": "http://127.0.0.1:8006",
            "description": "Development Server"
        }
    ]
)


# Root endpoint
@app.get("/")
def read_root():
    return {"Welcome": "user_service_api_main code"}