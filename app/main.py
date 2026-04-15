from fastapi import FastAPI
from app.db.database import engine, Base
from app.routes.student_routes import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)

app.include_router(student_router)