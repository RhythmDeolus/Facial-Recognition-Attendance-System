import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import sqlalchemy as db
from scripts.database.FaceRecog import FaceRecog
from models import Student, Face, Subject, Course, Timetable,\
        Semester, AcademicCalendar, CourseCalendarSemesterSemno, \
        TimetableCourseSemesterSemno
from sqlalchemy.ext.declarative import declarative_base


class RegisterDataAPI:
    def __init__(self):
        self.engine = db.create_engine(os.getenv('DB_URL'))
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine, checkfirst=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.session.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        self.session.commit()

    def registerSubject(self, course_id, name) -> Subject.id:
        subject = Subject(course_id=course_id, name=name)
        self.session.add(subject)
        self.session.commit()
        return subject.id

    def registerCourse(self, name) -> Course.id:
        course = Course(name=name)
        self.session.add(course)
        self.session.commit()
        return course.id

    def registerSemester(self, start_date, end_date) -> Semester.id:
        semester = Semester(start_date=start_date, end_date=end_date)
        self.session.add(semester)
        self.session.commit()
        return semester.id

    def registerAcademicCalendar(self, semester_id, course_id, start_date,
                                 end_date) -> AcademicCalendar.id:
        academic_calendar = AcademicCalendar(semester_id=semester_id,
                                             course_id=course_id,
                                             start_date=start_date,
                                             end_date=end_date)
        self.session.add(academic_calendar)
        self.session.commit()
        return academic_calendar.id

    def registerCourseCalendarSemesterSemno(self, academic_calendar_id,
                                            semester_id, course_id,
                                            semno) -> \
            CourseCalendarSemesterSemno.id:
        course_calendar_semester_semno = CourseCalendarSemesterSemno(
            academic_calendar_id=academic_calendar_id,
            semester_id=semester_id,
            course_id=course_id,
            semno=semno)
        self.session.add(course_calendar_semester_semno)
        self.session.commit()
        return course_calendar_semester_semno.id

    def registerTimetable(self, semester_id, course_id, semno) -> Timetable.id:
        timetable = Timetable(semester_id=semester_id, course_id=course_id,
                              semno=semno)
        self.session.add(timetable)
        self.session.commit()
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
        self.session.add(timetable_course_semester_semno)
        self.session.commit()
        return timetable_course_semester_semno.id

