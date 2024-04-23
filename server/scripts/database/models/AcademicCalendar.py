from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AcademicCalendar(Base):
    __tablename__ = 'academic_calendar'
    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)
    semester_id = Column(Integer, ForeignKey('semester.id'))
    semester = relationship('Semester', backref='academic_calendar')

    def __init__(self, year):
        self.year = year

    def __repr__(self):
        return f"<AcademicCalendar(academic_calendar_id=\
                {self.academic_calendar_id})>"
