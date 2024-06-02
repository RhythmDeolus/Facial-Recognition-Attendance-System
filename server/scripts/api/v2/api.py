from fastapi import FastAPI, Depends
from pydantic import BaseModel
from datetime import datetime, date, time
from typing import Annotated
from ...database.MainDataAPI import MainDataAPI
from .jwt import is_admin, is_teacher, ACCESS_TOKEN_EXPIRE_MINUTES, \
    Token, create_access_token, authenticate_user, authenticate_user_student, HTTPException, status, \
    OAuth2PasswordRequestForm, fake_users_db, timedelta, is_student, get_student_id

api = FastAPI()

database: MainDataAPI = None


def getDatabase() -> MainDataAPI:
    global database
    if database is None:
        database = MainDataAPI()
    return database


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
    user = authenticate_user(fake_users_db, form_data.username,
                             form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "role": "admin"}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@api.post("/student_token")
async def student_login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    user = authenticate_user_student(fake_users_db, form_data.username,
                             form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username, "role": "student"}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@api.post('/mark_attendance')
async def mark_attendance(body: AttendanceItem):
    res = getDatabase().getStudentFromFace(body.embedding)
    if res is not None:
        student_id = None
        embedding = None
        class_entry = None
        print(res)
        student_id, embedding = res.id, res.face_embedding
        if type(student_id) is not None:
            class_entry = getDatabase().markAttendance(student_id, body.time)
        if class_entry is False:
            return {'not_found': True}
        else:
            return {'id': student_id, 'end_time': class_entry.end_time}
    return {'not_found': True}


@api.post('/register_student_face')
async def register_student_face(valid: Annotated[bool, Depends(is_admin)],
                                body: StudentFaceItem):
    if not valid:
        return False
    res = getDatabase().registerStudentFace(body.id, body.image)
    return res


@api.post('/update_student_face')
async def update_student_face(valid: Annotated[bool, Depends(is_admin)],
                              body: StudentFaceItem):
    if not valid:
        return False
    res = getDatabase().update_embedding(body.id, body.image)
    return res


@api.post('/register_student')
async def register_student(valid: Annotated[bool, Depends(is_admin)],
                           id: int, name: str, course_id: int,
                           semester_id: int, semno: int):
    if not valid:
        return False
    res = getDatabase().registerStudent(student_id=id, name=name,
                                        course_id=course_id, semno=semno,
                                        semester_id=semester_id)
    return res

@api.get('/get_student')
async def get_student(valid: Annotated[bool, Depends(is_teacher)],
                      student_id: int):
    if not valid:
        return False
    res = getDatabase().getStudent(student_id)
    return {
        x.id: {
            "name": x.name,
            "course_id": x.course_id
        } for x in res
    }


@api.get('/get_students_for_course')
async def get_students_for_course(valid: Annotated[bool, Depends(is_admin)],
                                  course_id: int):
    if not valid:
        return False
    res = getDatabase().getStudentsForCourse(course_id)
    res = {x.id: {"name": x.name} for x in res}
    return res


@api.get('/get_attendance_for_subject')
async def get_attendance(valid: Annotated[bool, Depends(is_admin)],
                         subject_id: int):
    if not valid:
        return False
    res = getDatabase().getAttendanceForSubject(subject_id)
    res = {x.attendance_id: {"student_id": x.student_id,
                  "class_id": x.class_entry_id} for x in res}
    return res


@api.get('/get_attendance_for_student')
async def get_attendance(valid: Annotated[bool, Depends(is_student)],
                         student_id: Annotated[int, Depends(get_student_id)]):
    if not valid and subject_id is None:
        return False
    res = getDatabase().getAttendanceForStudent(student_id)
    res = {x.attendance_id: {
                "subject_id": x.class_entry.subject.id,
                "subject_name": x.class_entry.subject.name,
                  "class_id": x.class_entry_id, "start_time": x.class_entry.start_time,
                  "end_time": x.class_entry.end_time,
                  "date": x.class_entry.date
                  } for x in res}
    return res


@api.get('/get_classes_for_subject')
async def get_classes_for_subject(valid: Annotated[bool, Depends(is_admin)],
                                  subject_id: int,
                                  semester_id: int):
    if not valid:
        return False
    res = getDatabase().getClassesForSubject(subject_id, semester_id)
    res = {x.id: {
        "date": x.date,
        "start_time": x.start_time,
        "end_time": x.end_time,
        "academic_calendar_id": x.academic_calendar_id,
        "timetable_id": x.timetable_id
    } for x in res}
    return res

@api.get('/get_classes_for_subject_student')
async def get_classes_for_subject_student(valid: Annotated[bool, Depends(is_student)],
                                  subject_id: int,
                                  semester_id: int):
    if not valid:
        return False
    res = getDatabase().getClassesForSubject(subject_id, semester_id)
    res = {x.id: {
        "date": x.date,
        "start_time": x.start_time,
        "end_time": x.end_time,
        "academic_calendar_id": x.academic_calendar_id,
        "timetable_id": x.timetable_id
    } for x in res}
    return res



@api.post('/register_subject')
async def register_subject(valid: Annotated[bool, Depends(is_admin)],
                           name: str, course_id: int, code: int):
    if not valid:
        return False
    res = getDatabase().registerSubject(course_id, name, code)
    return res


@api.get('/get_subjects')
async def get_subjects(valid: Annotated[bool, Depends(is_teacher)],
                       course_id: int):
    if not valid:
        return False
    res = getDatabase().listSubjects(course_id)
    return {x.id: {"name": x.name, "desc": x.description} for x in res}


@api.post('/register_course')
async def register_course(valid: Annotated[bool, Depends(is_admin)],
                          name: str, description: str):
    if not valid:
        return False
    res = getDatabase().registerCourse(name, description)
    return res


@api.get('/get_courses')
async def get_courses(valid: Annotated[bool, Depends(is_teacher)]):
    if not valid:
        return False
    res = getDatabase().listCourses()
    res = {x.id: {"name": x.name,
                  "desc": x.description} for x in res}
    return res


@api.post('/register_semester')
async def register_semester(valid: Annotated[bool, Depends(is_admin)],
                            start_date: datetime, end_date: datetime):
    if not valid:
        return False
    res = getDatabase().registerSemester(start_date, end_date)
    return res


@api.get('/get_semesters')
async def get_semsters(valid: Annotated[bool, Depends(is_admin)]):
    if not valid:
        return False
    res = getDatabase().listSemsters()
    return {x.id: {
        "start_date": x.start_date,
        "end_date": x.end_date
    } for x in res}

@api.get('/get_semesters_student')
async def get_semsters_student(valid: Annotated[bool, Depends(is_student)]):
    if not valid:
        return False
    res = getDatabase().listSemsters()
    return {x.id: {
        "start_date": x.start_date,
        "end_date": x.end_date
    } for x in res}


@api.post('/register_academic_calendar')
async def register_academic_calendar(valid: Annotated[bool, Depends(is_admin)],
                                     semester_id: int):
    if not valid:
        return False
    res = getDatabase().registerAcademicCalendar(semester_id)
    return res


@api.post('/register_time_table')
async def register_time_table(valid: Annotated[bool, Depends(is_admin)]):
    if not valid:
        return False
    res = getDatabase().registerTimetable()
    return res


@api.post('/schedule_class')
async def schedule_class(valid: Annotated[bool, Depends(is_teacher)],
                         subject_id: int, date: datetime, start_time: datetime,
                         end_time: datetime,
                         academic_calendar_id: int, timetable_id: int):
    if not valid:
        return False
    res = getDatabase().registerClass(subject_id, date, start_time, end_time,
                                      academic_calendar_id,
                                      timetable_id)
    return res


@api.post('/register_calendar_course_semester_semno')
async def register_calendar_course_semester_semno(valid: Annotated[bool,
                                                  Depends(is_admin)],
                                                  academic_calendar_id: int,
                                                  semester_id: int,
                                                  course_id: int,
                                                  semno: int):
    if not valid:
        return False
        res = getDatabase() \
            .registerCourseCalendarSemesterSemno(academic_calendar_id,
                                                 semester_id, course_id,
                                                 semno)
        return res


@api.post('/register_timetable')
async def register_timetable(valid: Annotated[bool, Depends(is_admin)],
                             course_id: int, semester_id: int,
                             semno: int):
    if not valid:
        return False
    res = getDatabase().registerTimetable(
        course_id=course_id,
        semester_id=semester_id,
        semno=semno)
    return res


@api.post('/register_timetable_course_semester_semno')
async def register_timetable_course_semester_semno(valid: Annotated[bool,
                                                   Depends(is_admin)],
                                                   timetable_id: int,
                                                   semester_id: int,
                                                   course_id: int,
                                                   semno: int):
    if not valid:
        return False
    res = getDatabase().registerTimeTableCourseSemesterSemno(timetable_id,
                                                             semester_id,
                                                             course_id,
                                                             semno)
    return res


@api.post('/register_class')
async def register_class(valid: Annotated[bool, Depends(is_admin)],
                         subject_id: int, course_id: int,
                         semester_id: int, date: date,
                         semno: int,
                         start_time: time, end_time: time):
    if not valid:
        return False
    res = getDatabase().registerClass(subject_id, date, start_time,
                                      end_time, course_id, semester_id,
                                      semno)
    return res


@api.post('/assign_calendar_course')
async def assign_calendar_course(valid: Annotated[bool, Depends(is_admin)],
                                 course_id: int, calendar_id: int,
                                 semester_id: int, semno: int):
    if not valid:
        return False
    res = getDatabase().registerCourseCalendarSemesterSemno(calendar_id,
                                                            semester_id,
                                                            course_id, semno)
    return res


@api.get('/get_subjects_for_course')
async def get_subjects_for_course(valid: Annotated[bool, Depends(is_teacher)],
                                  course_id: int):
    if not valid:
        return False
    res = getDatabase().listSubjects(course_id)
    res = {x.id: {"name": x.name} for x in res}
    return res


@api.get('/get_semesters')
async def get_semesters(valid: Annotated[bool, Depends(is_teacher)]):
    if not valid:
        return False
    # TODO: Implement
    res = getDatabase().getSemesters()
    res = {
        x[0]: {
            "start_date": x[1],
            "end_date": x[2]
        } for x in res if len(x) >= 3
    }
    return res


@api.get('/get_academic_calendars')
async def get_academic_calendars(valid: Annotated[bool, Depends(is_teacher)],
                                 semester_id: int):
    if not valid:
        return False
    res = getDatabase().listCalendars(semester_id=semester_id)
    res = {x.id: {"semester_id": x.semester_id} for x in res}
    return res


@api.get('/get_timetables')
async def get_timetables(valid: Annotated[bool, Depends(is_teacher)]):
    if not valid:
        return False
    res = getDatabase().listTimeTables()
    res = {x.timetable_id: {
        'course_id': x.course_id,
        'semester_id': x.semester_id,
        'sem_no': x.sem_no
    } for x in res}
    return res


@api.get('/get_classes_for_subject')
async def get_classes_for_subject(valid: Annotated[bool, Depends(is_teacher)],
                                  subject_id: int):
    if not valid:
        return False
    # TODO: Implement
    res = getDatabase().getClassesForSubject(subject_id)
    res = {x[0]: {
        "date": x[1],
        "start_time": x[2],
        "end_time": x[3],
        "academic_calendar_id": x[4],
        "timetable_id": x[5]
    } for x in res if len(x) >= 6}
    return res
