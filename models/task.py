from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Task(BaseModel):
    title: str
    description: Optional[str] = None

class TaskInDB(Task):
    id: Optional[str] = Field(alias="_id")
