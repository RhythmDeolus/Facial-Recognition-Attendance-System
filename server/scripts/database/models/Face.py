from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy import mapped_column
from pgvector.sqlalchemy import Vector

# from .Base import Base

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Face(Base):
    __tablename__ = 'face_id'
    id = Column(Integer, autoincrement=True, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    # face_embedding = Column('face_embedding', String, nullable=False)
    face_embedding = Column('face_embedding', Vector(128), nullable=False)
    student = relationship('Student', backref='face')

    def __init__(self, student_id, face_embedding):
        self.student_id = student_id
        self.face_embedding = face_embedding

    def __repr__(self):
        return f"<Face(student_id={self.student_id},\
                face_embedding={self.face_embedding})>"
