import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import sqlalchemy as db
from scripts.database.FaceRecog import FaceRecog
from .models import Student, Face, Subject, Course, Timetable,\
        Semester, AcademicCalendar, CourseCalendarSemesterSemno, \
        TimetableCourseSemesterSemno
from sqlalchemy.ext.declarative import declarative_base
import dotenv
dotenv.load_dotenv()


class ListDataAPI:
    def __init__(self):
        self.engine = db.create_engine(os.getenv('DB_URL'))
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine, checkfirst=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None
        self._session().execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        self._session().commit()

    def _session(self):
        if self.session is None or self.session.is_active is False:
            self.session = self.Session()
        return self.session

    def listCourses(self) -> list[Course]:
        courses = self._session().query(Course).all()
        return courses

    def listSemsters(self) -> list[Semester]:
        semesters = self._session().query(Semester).all()
        return semesters

    def listSubjects(self, course_id) -> list[Subject]:
        subjects = self._session().query(Subject)\
            .filter(Subject.course_id == course_id).all()
        return subjects

    def listStudents(self, course_id) -> list[Student]:
        students = self._session().query(Student)\
            .filter(Student.course_id == course_id).all()
        return students

    def listCalendars(self, semester_id) -> list[AcademicCalendar]:
        calendars = self._session().query(AcademicCalendar)\
            .filter(AcademicCalendar.semester_id == semester_id).all()
        return calendars
