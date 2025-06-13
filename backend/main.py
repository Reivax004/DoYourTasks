from typing import Optional, List
from venv import logger
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from models import TaskCreate, TaskUpdate
from fastapi import APIRouter

from routes import (
    tasks
)
app = FastAPI()

app.include_router(tasks.router, tags=["tasks"])
