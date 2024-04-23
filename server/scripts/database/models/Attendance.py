from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Attendance(Base):
    __tablename__ = 'attendance'
    attendance_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship('Student', backref='attendance')
    class_entry_id = Column(Integer, ForeignKey('class_entry.id'))
    class_entry = relationship('ClassEntry', backref='attendance')

    def __init__(self, student_id, timetable_entry_id,
                 accademic_calender_entry_id):
        self.student_id = student_id
        self.timetable_entry_id = timetable_entry_id
        self.accademic_calender_entry_id = accademic_calender_entry_id

    def __repr__(self):
        return f"<Attendance(student_id={self.student_id}, time={self.time},\
                date={self.tdate})>"
