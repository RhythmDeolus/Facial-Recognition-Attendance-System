from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    title = Column(String(20), nullable=False)
    description = Column(String(50), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Course(name={self.name})>"
