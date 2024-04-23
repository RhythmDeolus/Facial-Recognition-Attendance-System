from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship('Course', backref='student')
    face_id = Column(Integer, ForeignKey('face_id.id'))
    face = relationship('Face', backref='student')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Student(name={self.name})>"
