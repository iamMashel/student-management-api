from fastapi import APIRouter

router = APIRouter(prefix="/students", tags=["Students"])

students = []

@router.get("/")
def get_students():
    return students

@router.post("/")
def create_student(student: dict):
    students.append(student)
    return {"message": "Student created", "student": student}