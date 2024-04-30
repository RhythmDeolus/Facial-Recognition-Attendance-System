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


class RegisterDataAPI:
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

    def registerSubject(self, course_id, name, code) -> Subject.id:
        subject = Subject(course_id=course_id, name=name, code=code)
        self._session().add(subject)
        self._session().commit()
        return subject.id

    def registerCourse(self, name, description) -> Course.id:
        course = Course(name=name, description=description)
        self._session().add(course)
        self._session().commit()
        return course.id

    def registerSemester(self, start_date, end_date) -> Semester.id:
        semester = Semester(start_date=start_date, end_date=end_date)
        self._session().add(semester)
        self._session().commit()
        return semester.id

    def registerAcademicCalendar(self, semester_id) -> AcademicCalendar.id:
        academic_calendar = AcademicCalendar(semester_id=semester_id)
        self._session().add(academic_calendar)
        self._session().commit()
        return academic_calendar.id

    def registerCourseCalendarSemesterSemno(self, academic_calendar_id,
                                            semester_id, course_id,
                                            semno) -> \
            CourseCalendarSemesterSemno.id:
        course_calendar_semester_semno = CourseCalendarSemesterSemno(
            academic_calendar_id=academic_calendar_id,
            semester_id=semester_id,
            course_id=course_id,
            sem_no=semno)
        self._session().add(course_calendar_semester_semno)
        self._session().commit()
        return course_calendar_semester_semno.id

    def registerTimetable(self, course_id, semester_id, semno) -> Timetable.id:
        timetable = Timetable()
        timetable_course_semester_semno = TimetableCourseSemesterSemno(
            timetable=timetable,
            semester_id=semester_id,
            course_id=course_id,
            sem_no=semno)
        self._session().add(timetable)
        self._session().add(timetable_course_semester_semno)
        self._session().commit()
        return timetable.id

    def registerTimeTableCourseSemesterSemno(self, timetable_id,
                                             semester_id, course_id,
                                             semno) -> \
            TimetableCourseSemesterSemno.id:
        timetable_course_semester_semno = TimetableCourseSemesterSemno(
            timetable_id=timetable_id,
            semester_id=semester_id,
            course_id=course_id,
            semno=semno)
        self._session().add(timetable_course_semester_semno)
        self._session().commit()
        return timetable_course_semester_semno.id


