from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from .database.DatabaseAPI import DatabaseAPI

api1 = FastAPI()


def getDatabase() -> DatabaseAPI:
    return api1.database


class AttendanceItem(BaseModel):
    embedding: list[float]
    time: datetime


class StudentFaceItem(BaseModel):
    id: int
    embedding: list[float]


class MarkedAttendanceResponse(BaseModel):
    id: int | None
    embedding: list[float] | None


@api1.post('/mark_attendance', response_model=MarkedAttendanceResponse)
async def mark_attendance(body: AttendanceItem):
    res = getDatabase().getStudentID(body.embedding)
    student_id = None
    embedding = None
    print(res)
    if type(res) is tuple:
        student_id, embedding = res
    if type(student_id) is not None:
        api1.database.mark_attendance(student_id, body.time)
    return {'id': student_id, 'embedding': embedding}


@api1.post('/register_student_face')
async def register_student_face(body: StudentFaceItem):
    res = getDatabase().registerStudent(body.embedding, body.id)
    return res


@api1.post('/update_student_face')
async def update_student_face(body: StudentFaceItem):
    res = getDatabase().update_embedding(body.id, body.embedding)
    return res

@api1.get('/get_students')
async def get_students():
    res = getDatabase().get_students()
    res = {x[0]: {"name": x[1]} for x in res if len(x) >= 2}
    return res

@api1.get('/get_attendance')
async def get_attendance():
    res = getDatabase().get_attendance()
    res = {x[0]: {"id": x[1], "time": x[2] } for x in res if len(x) >= 3}
    return res