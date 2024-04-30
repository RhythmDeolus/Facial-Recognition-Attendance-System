from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .Base import Base
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class TimetableCourseSemesterSemno(Base):
    __tablename__ = 'timetable_course_semester_semno'
    id = Column(Integer, autoincrement=True, primary_key=True)
    timetable_id = Column(Integer, ForeignKey('timetable.id'))
    timetable = relationship('Timetable',
                             backref='timetable_course_semester_semno')
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship('Course', backref='timetable_course_semester_semno')
    semester_id = Column(Integer, ForeignKey('semester.id'))
    semester = relationship('Semester',
                            backref='timetable_course_semester_semno')
    sem_no = Column(Integer, nullable=False)
    unique_timetable = UniqueConstraint('timetable_id')

    def __init__(self, timetable, course_id, semester_id, sem_no):
        self.timetable = timetable
        self.course_id = course_id
        self.semester_id = semester_id
        self.sem_no = sem_no

    def __repr__(self):
        return f"<Timetable_Course_Semester_Semno(timetable_id=\
                {self.timetable_id})>"
