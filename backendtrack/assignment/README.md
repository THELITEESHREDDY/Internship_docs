# firstcrud_api
This is the in memory crud app to understand how a simple backend works

# APIs

## GET /
Home
welcome to the server

## GET /health
Health
gets helath check of server

## GET /tasks
Get All Tasks
returns all tasks

## POST /tasks
Post Tasks
create a task

## GET /tasks/{id}
Get Task By Id


## PUT /tasks/{id}
Edit Task


## DELETE /tasks/{id} 
Delete Task


## these are end points in swagger UI

![alt text](./media/image.png)


## 🚀 How to Start the Project

Anyone cloning this repository can get up and running instantly. The database and tables will be generated automatically on your first run.


1. **Clone the repository:**

   ```bash
   git clone https://github.com/THELITEESHREDDY/firstcrud_api
   cd firstcrud_pi
   ```

2. **Set up a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```


3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the server:**

   ```bash
   uvicorn main:app --reload
   ```
   *The database layout file will be automatically generated instantly upon startup.*


## 💾 Database Architecture


### Why SQLite was Chosen

* **Zero Configuration**: Requires no external server setup, standalone background containers, or credential management.

* **File-Based**: Entirely contained in a local disk block, making it lightweight for development workflows.

* **Fast Testing**: Runs reliably inside a localized environment for prototype validation.


### Database File Storage Location

The active database file is stored locally within the project root directory as:
`./database.db`


### Database Viewer Screenshot

Below is a visual snapshot of the compiled tables verified through our local database tool:


![Database Viewer Schema](./media/image%20copy.png) 



### Example SQL Query Executed

Here is a raw SQL transaction executed against the database instance to search for specific keyword criteria:


```sql
SELECT task_table.id, task_table.title, task_table.done 
FROM task_table 
WHERE lower(task_table.title) LIKE lower('%milk%');
```


## PostgreSQL with Docker

Start the PostgreSQL database:

```bash
docker run --name taskdb \
  -e POSTGRES_PASSWORD=GET_FROM_YOUR_ENV \
  -e POSTGRES_DB=tasks \
  -p 5433:5432 \
  -v taskdata:/var/lib/postgresql \
  -d postgres
```

```bash
curl -i http://localhost:8000/tasks
``` 
returns 200 + rows straight from Postgres. 
```bash
curl -i http://localhost:8000/tasks/999 
``` 
returns 404 + the error JSON.


### Checking routes working with postgres container 
 ▕  127.0.0.1:40400 - "POST /task/create HTTP/1.1" 201  : done
 ▕  127.0.0.1:48012 - "GET /task/ HTTP/1.1" 200         : done
 ▕  127.0.0.1:35074 - "GET /task/1 HTTP/1.1" 200        : done
 ▕  127.0.0.1:50300 - "GET /task/2 HTTP/1.1" 404        : done
 ▕  127.0.0.1:42460 - "PUT /task/update_task/1 HTTP/1.1" 201 : done
 ▕  127.0.0.1:32982 - "GET /task/1 HTTP/1.1" 200             : done
 ▕  127.0.0.1:53742 - "GET /task/ HTTP/1.1" 200              : done
 ▕  127.0.0.1:46706 - "DELETE /task/delete/1 HTTP/1.1" 204   : done