import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import sqlalchemy as db
from scripts.database.FaceRecog import FaceRecog
from .models import Student, Face, Subject, Course, Timetable,\
        Semester, AcademicCalendar, CourseCalendarSemesterSemno, \
        TimetableCourseSemesterSemno, StudentSemesterSemno
from sqlalchemy.ext.declarative import declarative_base
import numpy as np
import dotenv
from functools import wraps
dotenv.load_dotenv()


def handle_error(value=None):
    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                print(e)
                args[0]._session().rollback()
                return value

        return inner

    return outer


class StudentDataAPI:
    def __init__(self):
        self.engine = db.create_engine(os.getenv('DB_URL'))
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine, checkfirst=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None
        self.fr = FaceRecog()
        self._session().execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        self._session().commit()

    def _session(self):
        if self.session is None or self.session.is_active is False:
            self.session = self.Session()
        return self.session

    @handle_error(False)
    def registerStudent(self, student_id, name, course_id, semno, semester_id):
        student = Student(id=student_id, name=name, course_id=course_id)
        student_semester_semno = StudentSemesterSemno(student_id=student_id,
                                                      semester_id=semester_id,
                                                      sem_no=semno)
        self._session().add(student)
        self._session().add(student_semester_semno)
        self._session().commit()
        return True

    def getStudent(self, student_id):
        return self._session().query(Student)\
            .filter(Student.id == student_id)\
            .first()

    def updateStudent(self, student_id, name):
        student = self.getStudent(student_id)
        student.name = name
        self._session().commit()

    @handle_error(False)
    def deleteStudent(self, student_id) -> bool:
        student = self.getStudent(student_id)
        self._session().delete(student)
        self._session().commit()

    @handle_error(False)
    def registerStudentFace(self, student_id, image) -> bool:
        image = self.fr.stringToArray(image)
        faces = self.fr.detectFaces(image)
        if len(faces) > 0:
            encodings = self.fr.getEncodings(image, [faces[0]])
            embedding = encodings[0]
            embedding = np.array(embedding)
            self._session().get(Student, student_id).face_embedding = embedding
            self._session().commit()
            return True
        return False

    def getStudentFromFace(self, face_embedding):
        student = self._session().query(Student)\
            .filter(Student.face_embedding.l2_distance(face_embedding) < 0.6)\
            .first()
        return student

    def getStudentsForCourse(self, course_id):
        return self._session().query(Student)\
            .filter(Student.course_id == course_id)\
            .all()

