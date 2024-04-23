from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StudentSemesterSemno(Base):
    __tablename__ = 'student_semester_semno'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship('Student', backref='student_semester_semno')
    semester_id = Column(Integer, ForeignKey('semester.id'))
    semester = relationship('Semester', backref='student_semester_semno')
    sem_no = Column(Integer, nullable=False)

    def __init__(self, student_id, semester_id, sem_no):
        self.student_id = student_id
        self.semester_id = semester_id
        self.sem_no = sem_no

    def __repr__(self):
        return f"<StudentSemesterSemno(student_id={self.student_id})>"
