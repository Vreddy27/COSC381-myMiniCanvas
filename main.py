from fastapi import FastAPI, HTTPException
from typing import List
from course import CourseManager
from user import UserManager

app = FastAPI()
course_manager = CourseManager()
user_manager = UserManager()

@app.get("/")
def welcome():
    return "Welcome to our miniCanvas!"

@app.post("/courses/{coursecode}")
def create_a_course(coursecode: str, request_body: dict):
    semester = request_body.get("semester")
    teacher_id_list = request_body.get("teacher_id_list")

    if not semester or not teacher_id_list:
        raise HTTPException(status_code=422, detail="Invalid payload. 'semester' and 'teacher_id_list' are required.")

    # Process the request and create the course
    course_id = course_manager.create_a_course(coursecode, semester, teacher_id_list)
    return {"course_id": course_id}

@app.put("/courses/{course_id}/students")
def import_students(course_id: int, request_body: dict):
    student_id_list = request_body.get("student_id_list")

    course = course_manager.find_a_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found")

    if not student_id_list:
        raise HTTPException(status_code=422, detail="Invalid payload. 'student_id_list' is required.")

    course.import_students(student_id_list)
    return {"message": "Students imported successfully."}