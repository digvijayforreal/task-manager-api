from fastapi import FastAPI
from models import Task
from database import tasks_collection
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
app = FastAPI()

@app.get("/")
def home():
    return{"message":"FastAPI IS RUNNING"}


@app.post("/task", status_code = 201)
def create_task(task:Task):
    task_data = task.model_dump()
    result = tasks_collection.insert_one(task_data)
    task_id = str(result.inserted_id)
    task_data["_id"] = task_id
    return{
        "message":"Task added successfully",
        "task_id": task_id,
        "task":task_data
    }
    
@app.get("/tasks")
def get_tasks():
    tasks = list(tasks_collection.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    
    return{
        "message": "Tasks retrieved successfully",
        "total_task": len(tasks),
        "task": tasks
    }


@app.get("/task/{task_id}")
def get_task(task_id:str):
    try:
        obj_id = ObjectId(task_id)
    
    except InvalidId:
        raise HTTPException(
            status_code = 400,
            detail= "Invalid task ID"
        )
    
    task = tasks_collection.find_one({"_id":obj_id})
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail = "Task not found"
        )
    
    task["_id"] = str(task["_id"])

    return {
        "message": "Task retrieved successfully",
        "task": task
    }

@app.put("/task/{task_id}")
def update_task(task_id: str, task: Task):

    # Convert string ID to ObjectId
    try:
        obj_id = ObjectId(task_id)

    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid task ID"
        )

    # Convert Pydantic model into dictionary
    task_data = task.model_dump()

    # Update document in MongoDB
    result = tasks_collection.update_one(
        {"_id": obj_id},
        {"$set": task_data}
    )

    # Check if the document exists
    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task updated successfully",
        "task_id": task_id,
        "updated_task": task_data
    }

@app.delete("/task/{task_id}")
def delete_task(task_id: str):

    # Convert task ID to ObjectId
    try:
        obj_id = ObjectId(task_id)

    except InvalidId:
        raise HTTPException(
            status_code=400,
            detail="Invalid task ID"
        )

    # Delete document from MongoDB
    result = tasks_collection.delete_one(
        {"_id": obj_id}
    )

    # Check whether a document was deleted
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully",
        "task_id": task_id
    }