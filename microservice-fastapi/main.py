from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Coursera"}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"result": total}

@app.get("/subtract/{num1}/{num2}")
async def subtract(num1: int, num2: int):
    """Subtract two numbers"""
    total = num1 - num2
    return {"result": total}

@app.get("/multiply/{num1}/{num2}")
async def multiply(num1: int, num2: int):
    """Multiply two numbers"""
    total = num1 * num2
    return {"result": total}


@app.get("/divide/{num1}/{num2}")
async def divide(num1: int, num2: int):
    """Divide two numbers"""
    total = num1 / num2
    return {"result": total}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
