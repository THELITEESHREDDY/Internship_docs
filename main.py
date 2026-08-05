from fastapi import FastAPI,status,HTTPException
from db_config import Base,engine
from models import Task
from routes import task_routes


Base.metadata.create_all(engine)

app = FastAPI(title="TASK_api")

app.include_router(task_routes)