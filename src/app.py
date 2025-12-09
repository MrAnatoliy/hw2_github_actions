from fastapi import FastAPI

from src.utils import adder

app = FastAPI()

@app.get("/health")
async def health_check():
    return {
        "health": "ok"
    }

@app.get("/add")
async def add_numbers(a: int, b: int):
    if not a or not b:
        return {
            "error": "a or b are undefinded"
        }
    return {
        "result": adder(a,b)
    }
    
@app.get("/mult")
async def mult_numbers(a: int, b: int):
    if not a or not b:
        return {
            "error": "a or b are undefinded"
        }
    return {
        "result": a * b
    }
    
@app.get("/div")
async def mult_numbers(a: int, b: int):
    if b == 0:
        return {
            "error": "cant divide by zero"
        }
    
    if not a or not b:
        return {
            "error": "a or b are undefinded"
        }
    return {
        "result": a / b
    }