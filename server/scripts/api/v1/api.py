from fastapi import FastAPI, Form, Depends
from pydantic import BaseModel
from datetime import datetime
from typing import Annotated
from ...database.DatabaseAPI import DatabaseAPI

api = FastAPI()


def getDatabase() -> DatabaseAPI:
    return api.database


class AttendanceItem(BaseModel):
    embedding: list[float]
    time: datetime


class StudentFaceItem(BaseModel):
    id: int
    image: str


class MarkedAttendanceResponse(BaseModel):
    id: int | None
    embedding: list[float] | None


class StudentItem(BaseModel):
    id: int
    name: str


@api.post('/register_student_face')
async def register_student_face(body: StudentFaceItem):
    res = getDatabase().registerStudentFace(body.image, body.id)
    return res


@api.post('/update_student_face')
async def update_student_face(body: StudentFaceItem):
    res = getDatabase().update_embedding(body.id, body.image)
    return res


@api.post('/register_student')
async def register_student(body: StudentItem):
    res = getDatabase().registerStudent(body.id, body.name)
    return res


@api.get('/get_students')
async def get_students():
    res = getDatabase().get_students()
    res = {x[0]: {"name": x[1]} for x in res if len(x) >= 2}
    return res


@api.get('/get_attendance')
async def get_attendance():
    res = getDatabase().get_attendance()
    res = {x[0]: {"id": x[1], "time": x[2] } for x in res if len(x) >= 3}
    return res