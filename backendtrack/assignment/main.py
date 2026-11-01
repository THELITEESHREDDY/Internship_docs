from fastapi import FastAPI,status,HTTPException
from assignment.db_config import Base,engine
from assignment.models import Task
from assignment.routes import task_routes
from assignment.settings import settings


Base.metadata.create_all(engine)
#print(settings.DB_CONNECTION)
app = FastAPI(title="TASK_api")

app.include_router(task_routes)
