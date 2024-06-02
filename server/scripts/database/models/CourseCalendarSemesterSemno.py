from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class CourseCalendarSemesterSemno(Base):
    __tablename__ = 'course_calendar_semester_semno'
    id = Column(Integer, autoincrement=True, primary_key=True)
    academic_calendar_id = Column(Integer, ForeignKey('academic_calendar.id'),
                                  nullable=False)
    academic_calendar = \
        relationship('AcademicCalendar')
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    course = relationship('Course')
    semester_id = Column(Integer, ForeignKey('semester.id'), nullable=False)
    semester = relationship('Semester')
    sem_no = Column(Integer, nullable=False)

    def __init__(self, academic_calendar_id, course_id, semester_id, sem_no):
        self.academic_calendar_id = academic_calendar_id
        self.course_id = course_id
        self.semester_id = semester_id
        self.sem_no = sem_no

    def __repr__(self):
        return f"<CourseCalendarSemesterSemno(course_calendar_id=\
                {self.academic_calendar_id})>"
