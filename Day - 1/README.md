# FastAPI Setup Guide for Beginners

## What is FastAPI?

FastAPI is a modern, fast web framework for building APIs with Python. It's designed to be easy to use, fast to code, and production-ready.

## Installation

### Step 1: Install Python
Make sure you have Python 3.8 or higher installed. Check your version:
```bash
python --version
```

### Step 2: Create a Project Directory
```bash
mkdir my-fastapi-app
cd my-fastapi-app
```

### Step 3: Create a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 4: Install FastAPI and Uvicorn
```bash
pip install fastapi uvicorn[standard]
```

## Your First FastAPI Application

Create a file called `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

## Running Your Application

Run the server with:
```bash
uvicorn main:app --reload
```

- `main` refers to the file `main.py`
- `app` refers to the FastAPI instance
- `--reload` enables auto-restart when code changes (development only)

Your API is now running at `http://127.0.0.1:8000`

## Interactive API Documentation

FastAPI automatically generates interactive API docs:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Common FastAPI Features

### 1. Path Parameters
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### 2. Query Parameters
```python
@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}
```

### 3. Request Body (POST requests)
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}
```

### 4. PUT/PATCH/DELETE Methods
```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated": True}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}
```

## Project Structure (Recommended)

```
my-fastapi-app/
├── venv/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── items.py
│   └── database.py
├── requirements.txt
└── README.md
```

## Useful Commands

```bash
# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Run with custom host/port
uvicorn main:app --host 0.0.0.0 --port 8080
```

## Next Steps

1. Learn about dependency injection
2. Add database integration (SQLAlchemy)
3. Implement authentication (OAuth2, JWT)
4. Add middleware for CORS, logging
5. Write tests with pytest
6. Deploy to production (Docker, cloud platforms)

## Resources

- Official Documentation: https://fastapi.tiangolo.com
- GitHub: https://github.com/tiangolo/fastapi
- Tutorial: https://fastapi.tiangolo.com/tutorial/