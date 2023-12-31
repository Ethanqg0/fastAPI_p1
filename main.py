"""
    how to run the server:
        uvicorn main:app --reload #run this in terminal to start server

    flags to add to the command:
        --reload: auto reloads the server when changes are made
        --host: specify host
        --port: specify port
        --workers: specify number of workers. workers are used to handle requests. the more
            workers, the more requests can be handled at once. the default is 1 worker per core
        --log-level: specify log level. default is info. this is important for receiving useful logging info
        --proxy-headers: Indicates whether Uvicorn should trust proxy headers or not. This is important when deploying behind a reverse proxy like Nginx or Apache.
        --proxy-protocol: Enables or disables support for the PROXY protocol, which is often used with load balancers and reverse proxies.
        --limit-concurrency: Limits the maximum number of concurrent connections to the server. This can be useful for controlling the load on your server.
        --limit-max-requests: Specifies the maximum number of requests per worker process before they are recycled. This can help manage memory usage.
        --limit-max-requests-jitter: Adds jitter to the maximum requests limit, which can help distribute load more evenly.
        --ssl-keyfile and --ssl-certfile: If you want to enable HTTPS, you can provide the paths to the SSL certificate and key files.
                
"""

"""
    General Notes
        FastAPI has very strong type checking. It will automatically convert types to the correct type
        FastAPI has great parameter path validation. You have fine grained control over the parameter values. This creates lot of control and validation.
        FastAPI has automatic documentation. It will automatically generate documentation for your API. This is very useful for other developers using your API. This is accomplished by swaggerUI
        FastAPI is designed for creating APIs, whereas Flask is designed for creating web applications. Flask is more flexible, but FastAPI is more structured.
        FastAPI is a better choice over Django when you want to create an API. Django is a better choice when you want to create a web application.
        Asynchronicity can be especially useful for building APIs because it enables concurrency and limits IO operations
        

"""

"""
fast api will be a fantastic choice for a website messaging application because well store the data inside an IO file and fastapi is great for io operations
additionally it will be good because it has two way communication so that the server can send messages to the client and the client can send messages to the server
"""

from fastapi import FastAPI, Path, Query, websockets #import fastAPI
from typing import Optional #used for optional parameters
from pydantic import BaseModel #pydantic is used for data validation
import uvicorn

app = FastAPI() #creates an instance of fastAPI

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    },
    2: {
        "name": "Jane",
        "age": 16,
        "year": "year 11"
    },
    3: {
        "name": "Bob",
        "age": 18,
        "year": "year 13"
    },
    4: {
        "name": "Alice",
        "age": 16,
        "year": "year 11"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}

# path parameters
@app.get("/get-student/{student_id}")
async def get_student( student_id: int = Path(..., description="Get a student", ge=2, le=3) ) -> dict:
    if student_id in students:
        return students[student_id]
    else:
        return {"message": "Student not found"}

# query parameters
@app.get("/get-by-name")
async def get_student(name: str, age: int) -> dict:
    for student_id, student in students.items():
        if student["name"] == name and student["age"] == age:
            return student
    return {"message": "Student not found"}

# query path parameters
@app.get("/get-student/qp/{student_id}")
async def get_student(
    student_id: int = Path(..., description="Get a student", ge=1, le=4),
    name: str = Query(None, description="Student's name"),
    age: int = Query(None, description="Student's age"),) -> dict:
    if student_id in students:
        student = students[student_id]
        if (name is None or student["name"] == name) and (age is None or student["age"] == age):
            return student
    return {"message": "Student not found"}

@app.post("/create-student/{student_id}")
async def create_student(student_id: int, student: Student) -> dict:
    if student_id in students:
        return {"message": "Student already exists"}
    students[student_id] = student
    return students[student_id]