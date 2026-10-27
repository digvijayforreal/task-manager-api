from models import Task

#created a object
task1 = Task(
    title = "Learn FastAPI",
    description = "Build a simple Task Manager API"
)

# print the task
print(task1)

# convert task to dictionary
task_dict = task1.model_dump()

print(task_dict)