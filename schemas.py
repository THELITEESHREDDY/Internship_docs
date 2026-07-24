from pydantic import BaseModel

class Task(BaseModel):
    title:str
    id:int
    done:bool 

class TaskRequest(BaseModel):
    title:str