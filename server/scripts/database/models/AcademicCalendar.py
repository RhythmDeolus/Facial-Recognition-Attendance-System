from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class AcademicCalendar(Base):
    __tablename__ = 'academic_calendar'
    id = Column(Integer, autoincrement=True, primary_key=True)
    semester_id = Column(Integer, ForeignKey('semester.id'), nullable=False)
    semester = relationship('Semester')

    def __init__(self, semester_id):
        self.semester_id = semester_id

    def __repr__(self):
        return f"<AcademicCalendar(academic_calendar_id=\
                {self.academic_calendar_id})>"
