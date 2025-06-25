# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from marking_ps_gemini import classify_problem_statement

app = FastAPI()

# 1. Define the shape of the incoming data
class PSRequest(BaseModel):
    idea: str
    problem_statement: str

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}

# 2. Switch to POST and take PSRequest as the body
@app.post("/evaluate_ps")
async def evaluate_problem_statement(request: PSRequest):
    # 3. Unpack and call your classifier
    result = classify_problem_statement(request.idea, request.problem_statement)

    return {
        "success": result.get("success", False),
        "Problem Statement": request.problem_statement,
        "Idea": request.idea,
        "data": result.get("data"),
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
