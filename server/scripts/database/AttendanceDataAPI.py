import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, desc
from types import NoneType
import sqlalchemy as db
from scripts.database.FaceRecog import FaceRecog
from sqlalchemy.ext.declarative import declarative_base
from .models import Student, Face, Attendance, StudentSemesterSemno, \
    Timetable, Subject, TimetableCourseSemesterSemno,\
    CourseCalendarSemesterSemno, AcademicCalendar, ClassEntry
import dotenv
from datetime import datetime 
dotenv.load_dotenv()


class AttendanceDataAPI:
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

    def markAttendance(self, student_id, time: datetime):
        # mark attendance byt getting semester and semno from StudentSemesterSemno
        # and then getting the timetable for that semester and semno from TimetableCourseSemesterSemno
        # and then getting the timetable entries for that timetable from TimetableEntry based on time
        # and then getting acadamic calander for that semester and semno and course from CourseCalendarSemesterSemno
        # and then getting the academic calander entry for that acadamic calander based on time
        # and then use them to check for attendance and mark it if not present

        # Grab the student
        student: Student = self._session().query(Student)\
                .filter(Student.id == student_id)\
                .first()
        if student is None:
            return False

        # Grab the student's semester and sem_no
        # order by sem_no to get the largest sem_no
        student_sem: StudentSemesterSemno = self._session()\
            .query(StudentSemesterSemno)\
            .filter(StudentSemesterSemno.student_id == student_id)\
            .order_by(desc(StudentSemesterSemno.sem_no)).first()
        if student_sem is None:
            return False

        # Grab the student's timetable
        timetable_course_semester_semno: TimetableCourseSemesterSemno =\
            self._session().query(TimetableCourseSemesterSemno)\
            .filter(TimetableCourseSemesterSemno.semester ==
                    student_sem.semester)\
            .filter(TimetableCourseSemesterSemno.sem_no == student_sem.sem_no)\
            .filter(TimetableCourseSemesterSemno.course_id ==
                    student.course_id)\
            .order_by(desc(TimetableCourseSemesterSemno.id))\
            .first()
        if timetable_course_semester_semno is None:
            return False
        # if timetable_entry is None:
        #     return False

        # Grab the student's academic calendar
        course_cal: CourseCalendarSemesterSemno =\
            self._session().query(CourseCalendarSemesterSemno)\
            .filter(CourseCalendarSemesterSemno.semester ==
                    student_sem.semester)\
            .filter(CourseCalendarSemesterSemno.sem_no ==
                    student_sem.sem_no)\
            .filter(CourseCalendarSemesterSemno.course_id ==
                    student.course_id)\
            .first()
        if course_cal is None:
            return False
        academic_cal: AcademicCalendar = course_cal.academic_calendar
        if academic_cal is None:
            return False

        # academic_cal_entry = \
        #     self._session().query(AcademicCalendarEntry)\
        #         .filter(AcademicCalendarEntry.academic_id ==
        #                 academic_cal.academic_id)\
        #         .filter(AcademicCalendarEntry.day == time.weekday())\
        #         .filter(AcademicCalendarEntry.is_class_day is True)\
        #         .first()
        # timetable: TimetableEntry = timetable_course_semester_semno.timetable
        # timetable_entry = self._session().query(TimetableEntry)\
        #     .filter(TimetableEntry.timetable_id == timetable.timetable_id)\
        #     .filter(TimetableEntry.start_time <= time)\
        #     .filter(TimetableEntry.end_time >= time)\
        #     .first()
        # if academic_cal_entry is None:
        #     return False

        # Grab the class entry based on the timetable and academic calendar
        class_entry: ClassEntry = self._session().query(ClassEntry)\
            .filter(ClassEntry.timetable_id == timetable_course_semester_semno\
                    .timetable_id)\
            .filter(ClassEntry.academic_calendar_id ==
                    course_cal.academic_calendar_id)\
            .filter(ClassEntry.date == time.date())\
            .filter(ClassEntry.start_time <= time.time())\
            .filter(ClassEntry.end_time >= time.time())\
            .first()

        if class_entry is None:
            return False

        attendance = self._session().query(Attendance)\
            .filter(Attendance.student_id == student_id)\
            .filter(Attendance.class_entry_id ==
                    class_entry.id)\
            .first()
        if attendance is not None:
            return class_entry
        attendance = Attendance(student_id=student_id, time=time,
                                class_entry_id=class_entry.id)
        self._session().add(attendance)
        self._session().commit()
        return class_entry

    def getAttendanceForStudent(self, student_id):
        return self._session().query(Attendance)\
            .filter(Attendance.student_id == student_id)\
            .all()

    def getAttendanceForSubject(self, subject_id):
        return self._session().query(Attendance)\
        .join(ClassEntry)\
        .filter(ClassEntry.subject_id == subject_id)\
        .all()
