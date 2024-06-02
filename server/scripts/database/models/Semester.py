from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import relationship
from .Base import Base


class Semester(Base):
    __tablename__ = 'semester'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Semester(sem_no={self.sem_no})>"
