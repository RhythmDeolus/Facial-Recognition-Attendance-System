from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from .Base import Base

# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class Attendance(Base):
    __tablename__ = 'attendance'
    attendance_id = Column(Integer, autoincrement=True, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship('Student', backref='attendance')
    class_entry_id = Column(Integer, ForeignKey('class_entry.id'))
    class_entry = relationship('ClassEntry', backref='attendance')
    time = Column(DateTime())
    unique = UniqueConstraint('class_entry', 'student_id')

    def __init__(self, student_id, class_entry_id, time):
        self.student_id = student_id
        self.class_entry_id = class_entry_id
        self.time = time

    def __repr__(self):
        return f"<Attendance student_id={self.student_id}/>"
