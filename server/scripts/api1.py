from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


api1 = FastAPI()


class AttendanceItem(BaseModel):
    embedding: list[float]
    time: datetime


@api1.post('/mark_attendance')
async def mark_attendance(body: AttendanceItem):
    student_id = api1.face_recog.getStudentID(body.embedding)
    if type(student_id) is not None:
        api1.face_recog.mark_attendance(student_id, body.time)
    return body
