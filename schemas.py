from pydantic import BaseModel,Field
from datetime import datetime, timezone

class TaskDB(BaseModel):
    title:str
    id:int
    done:bool 
    created_at:datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at:datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class TaskResponse(BaseModel):
    title:str
    id:int
    done:bool 

class TaskRequest(BaseModel):
    title:str
    done:bool = Field(default=False)

class TaskUpdateRequest(BaseModel):
    title:str
    done:bool 
    