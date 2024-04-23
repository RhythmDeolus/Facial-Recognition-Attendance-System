from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Timetable(Base):
    # __tablename__ = 'timetable'
    # id = Column(Integer, primary_key=True)
    # course_id = Column(Integer, ForeignKey('course.id'))
    # course = relationship('Course', backref='timetable')
    # semseter_id = Column(Integer, ForeignKey('semester.id'))
    # semester = relationship('Semester', backref='timetable')
    # sem_no = Column(Integer, nullable=False)
    # timetable_entry = relationship('TimetableEntry', backref='timetable')
    #
    # def __init__(self, course_id):
        # self.course_id = course_id
    __tablename__ = 'timetable'
    id = Column(Integer, primary_key=True)

    def __init__(self):
        pass

    def __repr__(self):
        return f"<Timetable(course_id={self.course_id})>"
