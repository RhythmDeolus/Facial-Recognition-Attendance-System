from sqlalchemy import Column, Integer, ForeignKey, Time, Date
from sqlalchemy.orm import relationship
from .Base import Base
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class ClassEntry(Base):
    __tablename__ = 'class_entry'
    id = Column(Integer, autoincrement=True, primary_key=True)
    timetable_id = Column(Integer, ForeignKey('timetable.id'))
    timetable = relationship('Timetable', backref='class_entry')
    academic_calendar_id = Column(Integer, ForeignKey('academic_calendar.id'))
    academic_calendar = relationship('AcademicCalendar', backref='class_entry')
    subject_id = Column(Integer, ForeignKey('subject.id'))
    subject = relationship('Subject', backref='class_entry')
    date = Column(Date(), nullable=False)
    start_time = Column(Time(), nullable=False)
    end_time = Column(Time(), nullable=False)

    def __init__(self, subject_id, date, start_time, end_time, academic_calendar_id, timetable_id):
        self.subject_id = subject_id
        self.academic_calendar_id = academic_calendar_id
        self.timetable_id = timetable_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"<ClassEntry(day={self.date}, start_time={self.start_time},\
        end_time={self.end_time})>"
