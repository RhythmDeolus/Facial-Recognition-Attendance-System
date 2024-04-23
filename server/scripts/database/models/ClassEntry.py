from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ClassEntry(Base):
    __tablename__ = 'class_entry'
    id = Column(Integer, primary_key=True)
    timetable_id = Column(Integer, ForeignKey('timetable.id'))
    timetable = relationship('Timetable', backref='class_entry')
    academic_calendar_id = Column(Integer, ForeignKey('academic_calendar.id'))
    academic_calendar = relationship('AcademicCalendar', backref='class_entry')
    subject_id = Column(Integer, ForeignKey('subject.id'))
    subject = relationship('Subject', backref='timetable_entry')
    date = Column(String(20), nullable=False)
    start_time = Column(String(20), nullable=False)
    end_time = Column(String(20), nullable=False)
    semester_id = Column(Integer, ForeignKey('semester.id'))
    semester = relationship('Semester', backref='class_entry')
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship('Course', backref='class_entry')

    def __init__(self, subject_id, date, start_time, end_time, semester_id,
                 course_id, academic_calendar_id, timetable_id):
        self.subject_id = subject_id
        self.academic_calendar_id = academic_calendar_id
        self.timetable_id = timetable_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.semester_id = semester_id
        self.course_id = course_id

    def __repr__(self):
        return f"<ClassEntry(day={self.date}, start_time={self.start_time},\
        end_time={self.end_time})>"
