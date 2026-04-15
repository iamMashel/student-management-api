from fastapi import FastAPI
from app.routes.student_routes import router as student_router

app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)

app.include_router(student_router)

@app.get("/")
def root():
    return {"message": "Student Management API is running"}