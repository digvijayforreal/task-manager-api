from pydantic import BaseModel

class Task(BaseModel):
    # Define the four fields 
    
        title: str
        description: str
        completed: bool = False
        priority: str = "medium"
    