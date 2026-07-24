from fastapi import FastAPI,status,HTTPException

from schemas import Task


tasks=[
    {"id":101,"title":"lala", "done":False},
    {"id":102, "title": "cheyale", "done":True}
]
app = FastAPI()

@app.get("/")
def home():
    return { 
        "name": "Task API", 
        "version": "1.0", 
        "endpoints": ["/tasks"] 
    }

@app.get("/health")
def health():
    return {
        "status" : "ok"
    }


@app.get("/tasks", 
    response_model=list[Task]
)
def get_all_tasks()->list[Task]:
    return tasks

@app.get("/tasks/{id}")
def get_task_by_id(id:int)->Task:

    required_task = None

    for task in tasks:
        if task["id"]==id:
            required_task=task


    if required_task is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"            
        )
    
    required_task_obj = Task(

        title=required_task["title"],
        id=required_task["id"],
        done=required_task["done"]

    )
    return required_task_obj