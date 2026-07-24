from fastapi import FastAPI,status,HTTPException

from schemas import Task,TaskRequest


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
)
def get_all_tasks():
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


@app.post("/tasks")
def post_tasks(task:TaskRequest):
    if task is None or len(task.title)<3:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Invalid task"
        )

    tasks.append({"id": len(tasks) ,"title":task.title, "completed" : False})

    return task