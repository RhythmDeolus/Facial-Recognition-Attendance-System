from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from .Base import Base
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)
    course = relationship('Course', backref='student')
    face_embedding = Column('face_embedding', Vector(128), nullable=True)

    def __init__(self, id, name, course_id):
        self.name = name
        self.id = id
        self.course_id = course_id

    def __repr__(self):
        return f"<Student(name={self.name})>"
