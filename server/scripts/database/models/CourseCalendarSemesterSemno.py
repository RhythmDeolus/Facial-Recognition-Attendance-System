from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CourseCalendarSemesterSemno(Base):
    __tablename__ = 'course_calendar_semester_semno'
    id = Column(Integer, primary_key=True)
    academic_calendar_id = Column(Integer, ForeignKey('academic_calendar.id'))
    academic_calendar = relationship('AcademicCalendar',
                                     backref='course_calendar_semester_semno')
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship('Course', backref='course_calendar_semester_semno')
    semester_id = Column(Integer, ForeignKey('semester.id'))
    semseter = relationship('Semester',
                            backref='course_calendar_semester_semno')
    sem_no = Column(Integer, nullable=False)

    def __init__(self, academic_calendar_id, course_id, semester_id, sem_no):
        self.academic_calendar_id = academic_calendar_id
        self.course_id = course_id
        self.semester_id = semester_id
        self.sem_no = sem_no

    def __repr__(self):
        return f"<CourseCalendarSemesterSemno(course_calendar_id=\
                {self.academic_calendar_id})>"
