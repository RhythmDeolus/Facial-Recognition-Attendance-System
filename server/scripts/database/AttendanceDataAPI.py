import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, desc
import sqlalchemy as db
from scripts.database.FaceRecog import FaceRecog
from sqlalchemy.ext.declarative import declarative_base
from models import Student, Face, Attendance, StudentSemesterSemno, TimeTable,\
        Subject, TimetableCourseSemesterSemno,\
        CourseCalendarSemesterSemno, AcademicCalendar, ClassEntry


class AttendanceDataAPI:
    def __init__(self):
        self.engine = db.create_engine(os.getenv('DB_URL'))
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine, checkfirst=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.session.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        self.session.commit()
        self.fr = FaceRecog()

    def markAttendance(self, student_id, time):
        # mark attendance byt getting semester and semno from StudentSemesterSemno
        # and then getting the timetable for that semester and semno from TimetableCourseSemesterSemno
        # and then getting the timetable entries for that timetable from TimetableEntry based on time
        # and then getting acadamic calander for that semester and semno and course from CourseCalendarSemesterSemno
        # and then getting the academic calander entry for that acadamic calander based on time
        # and then use them to check for attendance and mark it if not present

        # Grab the student
        student: Student = self.session.query(Student)\
                .filter(Student.id == student_id)\
                .first()
        if student is None:
            return False

        # Grab the student's semester and sem_no
        # order by sem_no to get the largest sem_no
        student_sem: StudentSemesterSemno = self.session\
            .query(StudentSemesterSemno)\
            .filter(StudentSemesterSemno.student_id == student_id)\
            .orderBy(desc(StudentSemesterSemno.sem_no)).first()
        if student_sem is None:
            return False

        # Grab the student's timetable
        timetable_course_semester_semno: TimetableCourseSemesterSemno =\
            self.session.query(TimetableCourseSemesterSemno)\
            .filter(TimetableCourseSemesterSemno.semester ==
                    student_sem.semester)\
            .filter(TimetableCourseSemesterSemno.semno == student_sem.semno)\
            .filter(TimetableCourseSemesterSemno.course_id ==
                    student.course_id)\
            .orderBy(desc(TimetableCourseSemesterSemno.id))\
            .first()
        if timetable_course_semester_semno is None:
            return False
        # if timetable_entry is None:
        #     return False

        # Grab the student's academic calendar
        course_cal: CourseCalendarSemesterSemno =\
            self.session.query(CourseCalendarSemesterSemno)\
            .filter(CourseCalendarSemesterSemno.semester ==
                    student_sem.semester)\
            .filter(CourseCalendarSemesterSemno.semno ==
                    student_sem.semno)\
            .filter(CourseCalendarSemesterSemno.course_id ==
                    student.course_id)\
            .first()
        if course_cal is None:
            return False
        academic_cal = course_cal.academic_calendar
        if academic_cal is None:
            return False

        # academic_cal_entry = \
        #     self.session.query(AcademicCalendarEntry)\
        #         .filter(AcademicCalendarEntry.academic_id ==
        #                 academic_cal.academic_id)\
        #         .filter(AcademicCalendarEntry.day == time.weekday())\
        #         .filter(AcademicCalendarEntry.is_class_day is True)\
        #         .first()
        # timetable: TimetableEntry = timetable_course_semester_semno.timetable
        # timetable_entry = self.session.query(TimetableEntry)\
        #     .filter(TimetableEntry.timetable_id == timetable.timetable_id)\
        #     .filter(TimetableEntry.start_time <= time)\
        #     .filter(TimetableEntry.end_time >= time)\
        #     .first()
        # if academic_cal_entry is None:
        #     return False

        # Grab the class entry based on the timetable and academic calendar
        class_entry: ClassEntry = self.session.query(ClassEntry)\
            .filter(ClassEntry.timetable_id == timetable_course_semester_semno
                    .timetable_id)\
            .filter(ClassEntry.academic_calendar_id ==
                    course_cal.academic_calendar_id)\
            .filter(ClassEntry.start_time <= time)\
            .filter(ClassEntry.end_time >= time)\
            .first()

        if class_entry is not None:
            return False

        attendance = self.session.query(Attendance)\
            .filter(Attendance.student_id == student_id)\
            .filter(Attendance.class_entry_id ==
                    class_entry.id)\
            .first()
        if attendance is not None:
            return True
        attendance = Attendance(student_id=student_id, time=time,
                                class_entry_id=class_entry.id)
        self.session.add(attendance)
        self.session.commit()

    def getAttendanceOfStudent(self, student_id):
        return self.session.query(Attendance)\
            .filter(Attendance.student_id == student_id)\
            .all()

    def getAttendanceOfSubject(self, subject_id):
        return self.session.query(Attendance)\
            .filter(Attendance.timetable_entry.subject_id == subject_id)\
            .all()
