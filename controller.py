from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from models import Task
from schemas import TaskResponse,TaskRequest,TaskDB, TaskUpdateRequest
from datetime import datetime,timezone


def create_task(task:TaskRequest,db:Session):
    data = task.model_dump()
    print(data)
    new_task = Task(
        title=data["title"],
        done=data["done"],
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_tasks(db:Session,offset:Optional[int]=0,limit:Optional[int]=10,done:Optional[bool]=None,search:Optional[str]=None):
    tasks=[]
    if done and search:
        search_filter = f"%{search}%"
        tasks=db.query(Task).filter(Task.done==done and Task.title.ilike(search_filter)).all()
    elif done :
        tasks=db.query(Task).filter(Task.done==done).all()
    elif search : 
        search_filter = f"%{search}%"
        tasks=db.query(Task).filter(Task.title.ilike(search_filter)).all()
    else:
        tasks=db.query(Task).all()

    return tasks

def get_task(task_id:int,db:Session)->TaskResponse:
    task = db.query(Task).filter(Task.id==task_id).first()

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task id is incorrect"
                            )
    return task

def update_tasks(body:TaskUpdateRequest,task_id:int,db:Session)->TaskResponse:
    task:Task = db.query(Task).filter(Task.id==task_id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No task with this id"
        )

    body = body.model_dump()

    for key,val in body.items():
        setattr(task,key ,val)

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def delete_task(task_id:int,db:Session)->None:

    task = db.query(Task).filter(Task.id==task_id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    db.delete(task)

    return None