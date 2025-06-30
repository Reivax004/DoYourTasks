from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

from Enum.priorite import PrioriteEnum


class TaskCreate(BaseModel):
    theme : Optional[str] = None
    description : str
    completed : bool = False
    priorite : Optional[PrioriteEnum]
    deadline : Optional[date]
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "theme": "travail",
                    "description": "reviser",
                    "completed" : False,
                    "priorite" : "basse",
                    "deadline" : "2019-12-04"
                }
            ]
        }
    )

class Task(TaskCreate):
    id : int
    created_at : datetime = Field(default_factory=datetime.now)
    
class TaskUpdate(Task):
    pass

class TaskResponse(Task):
    pass
