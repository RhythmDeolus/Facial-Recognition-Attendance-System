import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import sqlalchemy as db
from scripts.database.FaceRecog import FaceRecog
from sqlalchemy.ext.declarative import declarative_base
from .models import ClassEntry, AcademicCalendar, CourseCalendarSemesterSemno,\
    Timetable, TimetableCourseSemesterSemno
from datetime import datetime
import dotenv
dotenv.load_dotenv()


class ClassDataAPI:
    def __init__(self):
        self.engine = db.create_engine(os.getenv('DB_URL'))
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine, checkfirst=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None
        self._session().execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        self._session().commit()
        self.fr = FaceRecog()

    def _session(self):
        if self.session is None or self.session.is_active is False:
            self.session = self.Session()
        return self.session

    def registerClass(self, subject_id, date, start_time, end_time,
                      course_id, semester_id, semno):
        course_calendar_sem = self._session()\
            .query(CourseCalendarSemesterSemno)\
            .filter(CourseCalendarSemesterSemno.semester_id == semester_id)\
            .filter(CourseCalendarSemesterSemno.course_id == course_id)\
            .filter(CourseCalendarSemesterSemno.sem_no == semno)\
            .first()
        calendar_id = course_calendar_sem.academic_calendar_id
        timetable_course_sem = self._session()\
            .query(TimetableCourseSemesterSemno)\
            .filter(TimetableCourseSemesterSemno.course_id == course_id)\
            .filter(TimetableCourseSemesterSemno.semester_id == semester_id)\
            .filter(TimetableCourseSemesterSemno.sem_no == semno)\
            .first()

        timetable_id = timetable_course_sem.timetable_id
        class_entry = ClassEntry(subject_id=subject_id, date=date,
                                 start_time=start_time, end_time=end_time,
                                 academic_calendar_id=calendar_id,
                                 timetable_id=timetable_id)
        self._session().add(class_entry)
        self._session().commit()
        return class_entry.id

    def getClassesForSubject(self, subject_id: int, semester_id: int):
        return self._session().query(ClassEntry)\
            .join(AcademicCalendar, AcademicCalendar.id == ClassEntry.academic_calendar_id)\
            .filter(AcademicCalendar.semester_id == semester_id)\
            .filter(ClassEntry.subject_id == subject_id)\
            .filter(ClassEntry.date <= datetime.now().date())\
            # .filter(ClassEntry.end_time <= datetime.now().time()).all()
