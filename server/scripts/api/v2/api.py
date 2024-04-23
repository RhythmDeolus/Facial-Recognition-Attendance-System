from fastapi import FastAPI, Form, Depends
from pydantic import BaseModel
from datetime import datetime
from typing import Annotated
from ...database.DatabaseAPI import DatabaseAPI
from passlib.context import CryptContext
from .jwt import *;

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


@api.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@api.post('/mark_attendance', response_model=MarkedAttendanceResponse)
async def mark_attendance(body: AttendanceItem):
    res = getDatabase().getStudentIDFromFace(body.embedding)
    if res is not None:
        student_id = None
        embedding = None
        print(res)
        if type(res) is tuple:
            student_id, embedding = res
        if type(student_id) is not None:
            api.database.mark_attendance(student_id, body.time)
    return {'id': student_id, 'embedding': embedding}



@api.post('/register_student_face')
async def register_student_face(valid: Annotated[bool, Depends(is_admin)], body: StudentFaceItem):
    if not valid:
        return False
    res = getDatabase().registerStudentFace(body.image, body.id)
    return res


@api.post('/update_student_face')
async def update_student_face(valid: Annotated[bool, Depends(is_admin)], body: StudentFaceItem):
    if not valid:
        return False
    res = getDatabase().update_embedding(body.id, body.image)
    return res


@api.post('/register_student')
async def register_student(valid: Annotated[bool, Depends(is_admin)], body: StudentItem):
    if not valid:
        return False
    res = getDatabase().registerStudent(body.id, body.name)
    return res


@api.get('/get_students')
async def get_students(valid: Annotated[bool, Depends(is_teacher)]):
    if not valid:
        return False
    res = getDatabase().get_students()
    res = {x[0]: {"name": x[1]} for x in res if len(x) >= 2}
    return res

@api.get('/get_attendance')
async def get_attendance(valid: Annotated[bool, Depends(is_teacher)]):
    if not valid:
        return False
    res = getDatabase().get_attendance()
    res = {x[0]: {"id": x[1], "time": x[2] } for x in res if len(x) >= 3}
    return res
