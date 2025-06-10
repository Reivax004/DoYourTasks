from typing import Optional, List
from venv import logger
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from DoYourTasks.models import TaskCreate, TaskUpdate
from fastapi import APIRouter

from DoYourTasks.routes import (
    tasks
)
app = FastAPI()

app.include_router(tasks.router, tags=["tasks"])
