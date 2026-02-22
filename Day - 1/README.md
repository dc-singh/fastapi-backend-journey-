# The First API Setup
These are the simple steps to setup the FASTAPI in your system.

## Create the Virtual Environment
```
python -m env environment_name
```
This command will create a virtual environment in your current folder/directory.

## Activate The Virtual Environment
- for Mac
```
source venv/bin/activate
```
- for Windows
```
venv\Scripts\activate
```
**replace venv with your virtual environment name**

You'll see (venv) appear in your terminal prompt.

# Create Python file

let's make your first api in **FASTAPI**, but before that create a python file called main.py

Inside your python file paste the code below.

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world"}

@app.get("/blog") 
def blog():
    return{"Blog": "The First Blog"}
```

After That,
Open terminal in vs code, Run the code using this command,


`uvicorn main:app --reload`

Open your browser & go to the 

`http://127.0.0.1:8000/`

