import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Get MongoDB connection string
MONGO_URI = os.getenv("MONGODB_URI")

if not MONGO_URI:
    raise ValueError("MONGODB_URI not found in .env")

# Create MongoDB client
client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

# Select database
db = client["task_manager_db"]

# Select collection
tasks_collection = db["tasks"]

# Test database connection
if __name__ == "__main__":
    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")
    except Exception as e:
        print("MongoDB connection failed:", e)