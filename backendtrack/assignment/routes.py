from fastapi import APIRouter,HTTPException,status,Depends
from typing import List,Annotated
from sqlalchemy.orm import Session
from schemas import TaskDB,TaskRequest,TaskResponse,TaskUpdateRequest
from db_config import get_db
import controller

task_routes = APIRouter(prefix="/task")

@task_routes.post("/create",
                 response_model=TaskResponse,
                 status_code=status.HTTP_201_CREATED
                )
def create_task(
    task:TaskRequest,
    db:Session=Depends(get_db)
):
    print(task)
    return controller.create_task(task,db)


@task_routes.get("/",
                response_model=List[TaskResponse],
                status_code=status.HTTP_200_OK
                )
def get_tasks(offset:int|None = None,limit:int|None=None,done:bool|None=None,search:str|None = None,db:Session=Depends(get_db),):
    return controller.get_tasks(db,offset,limit,done,search)



@task_routes.get("/{task_id}",
                 response_model=TaskResponse,
                 status_code=status.HTTP_200_OK
                )
def get_task(task_id:int,db:Session=Depends(get_db)):
    return controller.get_task(task_id,db)


@task_routes.put("/update_task/{task_id}",
                 response_model=TaskResponse,
                 status_code=status.HTTP_201_CREATED
                )
def update_task(
    body:TaskUpdateRequest, 
    task_id:int,
    db:Session=Depends(get_db)
):
    return controller.update_tasks(body,task_id,db)

@task_routes.delete("/delete/{task_id}",
                    response_model=None,
                    status_code=status.HTTP_204_NO_CONTENT
                )
def delete_task(
    task_id:int,
    db:Session=Depends(get_db)
):
    return controller.delete_task(task_id,db)