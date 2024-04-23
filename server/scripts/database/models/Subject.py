from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship('Course', backref='subject')

    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

    def __repr__(self):
        return f"<Subject(name={self.name})>"
