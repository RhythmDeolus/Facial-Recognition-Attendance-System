from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Semester(Base):
    __tablename__ = 'semester'
    id = Column(Integer, primary_key=True)
    timetable = relationship('Timetable', backref='semester')
    start_date = Column(String(20), nullable=False)
    end_date = Column(String(20), nullable=False)

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Semester(sem_no={self.sem_no})>"
