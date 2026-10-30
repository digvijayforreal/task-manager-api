# Task Manager API

**A RESTful Task Management API built with Python, FastAPI, Pydantic, and MongoDB Atlas.**

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB%20Atlas-green.svg)](https://www.mongodb.com/atlas)
[![Pydantic](https://img.shields.io/badge/Validation-Pydantic-red.svg)](https://docs.pydantic.dev/)
[![API](https://img.shields.io/badge/Architecture-REST%20API-orange.svg)](https://fastapi.tiangolo.com/)

## Overview

Task Manager API is a backend application designed to manage tasks through RESTful API endpoints.

Built using FastAPI and MongoDB Atlas, the application allows users to create, retrieve, update, and delete tasks while maintaining persistent data storage.

Pydantic is used to validate incoming task data, while MongoDB stores task records and provides database operations.

The project demonstrates fundamental backend development concepts, including REST API design, database integration, request validation, HTTP status codes, and error handling.

## Key Features

### 1. Create Tasks

- Create new tasks through POST requests.
- Validate incoming data using Pydantic.
- Store tasks in MongoDB Atlas.
- Generate a unique MongoDB ObjectId for each task.
- Return the created task and its ID.

### 2. Retrieve All Tasks

- Fetch all stored tasks.
- Return the total number of tasks.
- Convert MongoDB ObjectIds into strings for JSON responses.

### 3. Retrieve a Specific Task

- Fetch an individual task using its ID.
- Validate MongoDB ObjectId format.
- Return HTTP 400 for invalid IDs.
- Return HTTP 404 when a task does not exist.

### 4. Update Tasks

- Update an existing task using its ID.
- Validate the task ID.
- Update task fields using MongoDB's `$set` operation.
- Return appropriate errors when the task is not found.

### 5. Delete Tasks

- Delete a task using its unique ID.
- Validate the supplied ID.
- Return HTTP 404 if the task does not exist.
- Confirm successful deletion.

## Task Data Model

Each task contains the following fields:

| Field | Data Type | Default |
|---|---|---|
| title | String | Required |
| description | String | Required |
| completed | Boolean | False |
| priority | String | Medium |

Example task:

```json
{
  "title": "Learn FastAPI",
  "description": "Build a Task Manager API",
  "completed": false,
  "priority": "medium"
}
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/task` | Create a task |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/task/{task_id}` | Retrieve a specific task |
| PUT | `/task/{task_id}` | Update a task |
| DELETE | `/task/{task_id}` | Delete a task |

## API Examples

### 1. Create a Task

**POST** `/task`

Request:

```json
{
  "title": "Learn Python",
  "description": "Practice Python programming",
  "completed": false,
  "priority": "high"
}
```

Response:

```json
{
  "message": "Task added successfully",
  "task_id": "YOUR_GENERATED_OBJECT_ID",
  "task": {
    "title": "Learn Python",
    "description": "Practice Python programming",
    "completed": false,
    "priority": "high"
  }
}
```

### 2. Retrieve All Tasks

**GET** `/tasks`

Returns all stored tasks along with their total count.

### 3. Retrieve a Specific Task

**GET** `/task/{task_id}`

Pass the task's MongoDB ObjectId in the URL.

### 4. Update a Task

**PUT** `/task/{task_id}`

Request:

```json
{
  "title": "Learn FastAPI",
  "description": "Build REST APIs using FastAPI",
  "completed": true,
  "priority": "high"
}
```

### 5. Delete a Task

**DELETE** `/task/{task_id}`

Deletes the task associated with the supplied ID.

## Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python 3.12+ |
| Backend Framework | FastAPI |
| Data Validation | Pydantic |
| Database | MongoDB Atlas |
| Database Driver | PyMongo |
| Environment Variables | Python-dotenv |
| Package Manager | uv |
| API Architecture | REST |

## Project Structure

```text
task-manager-api/
│
├── src/
│   └── task_manager_api/
│
├── main.py
├── database.py
├── models.py
├── test_model.py
│
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12 or higher
- uv package manager
- MongoDB Atlas account
- MongoDB connection string

### 1. Clone the Repository

```bash
git clone https://github.com/digvijayforreal/task-manager-api.git

cd task-manager-api
```

### 2. Install Dependencies

```bash
uv sync
```

### 3. Configure Environment Variables

Create a `.env` file in the project root.

```env
MONGODB_URI=your_mongodb_connection_string
```

Replace the placeholder with your MongoDB Atlas connection string.

Never commit your `.env` file or expose your database credentials.

### 4. Run the Application

```bash
uv run uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation.

Once the application is running, open:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

You can test all available endpoints directly through Swagger UI.

## Database Configuration

The application connects to MongoDB Atlas using PyMongo.

**Database:** `task_manager_db`

**Collection:** `tasks`

The MongoDB connection is configured using the `MONGODB_URI` environment variable.

## Error Handling

The API handles common errors:

| HTTP Status | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Task created successfully |
| 400 | Invalid task ID |
| 404 | Task not found |

## Learning Objectives

This project demonstrates practical implementation of:

- Building RESTful APIs using FastAPI.
- Defining data models using Pydantic.
- Connecting Python applications to MongoDB Atlas.
- Performing CRUD operations.
- Working with MongoDB ObjectIds.
- Handling HTTP exceptions.
- Managing environment variables.
- Running and testing backend applications.

## Future Improvements

- User authentication and authorization.
- Per-user task management.
- Task filtering and searching.
- Pagination and sorting.
- Due dates and task reminders.
- Task status management.
- Automated API testing with Pytest.
- Improved API validation and response schemas.

## Author

**Digvijay Mali**

GitHub: [@digvijayforreal](https://github.com/digvijayforreal)

Project: [Task Manager API](https://github.com/digvijayforreal/task-manager-api)

---

**Built with Python, FastAPI, Pydantic, and MongoDB Atlas.**