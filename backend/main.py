from typing import Optional, List
from venv import logger
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from models import TaskCreate, TaskUpdate
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware

from routes import (
    tasks
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pour tests locaux
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, tags=["tasks"])
