from fastapi import FastAPI


app = FastAPI()

@app.get("/hello")
def greet(user:str, age:str):
    return {"messages": f"Hello {user}, your age: {age}"}

@app.get("/square/{square}")
def square(square:int):
    return square**2

@app.get("/greet")
def greet(name:str,mood:str):
    if mood == "angry":
        return f"hello {name}, Just calm down bro, you are in {mood} mood"
    elif mood == "calm" or mood == "cool":
        return f"hello {name}, good to know that you're in {mood}"
    elif mood == "neutral":
        return f"hello {name}, want to do something crazy in this {mood} mood"
    else:
        return f"hello Mr. {name}"

@app.get("/add")
def cal(a:int, b:int,):
    return {f"The sum of {a} and {b} is: ": f"{a+b}"}
    
