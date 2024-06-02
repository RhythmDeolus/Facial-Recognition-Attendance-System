from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .Base import Base


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship('Course', backref='subject')
    code = Column(Integer, nullable=False)

    def __init__(self, name, course_id, code):
        self.name = name
        self.course_id = course_id
        self.code = code

    def __repr__(self):
        return f"<Subject(name={self.name})>"
