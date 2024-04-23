import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import sqlalchemy as db
from scripts.database.FaceRecog import FaceRecog
from models import Student, Face
from sqlalchemy.ext.declarative import declarative_base


class StudentDataAPI:
    def __init__(self):
        self.engine = db.create_engine(os.getenv('DB_URL'))
        self.Base = declarative_base()
        self.Base.metadata.create_all(self.engine, checkfirst=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.session.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        self.session.commit()

    def registerStudent(self, student_id, name):
        student = Student(id=student_id, name=name)
        self.session.add(student)
        self.session.commit()

    def getStudent(self, student_id):
        return self.session.query(Student).filter(Student.id == student_id)\
                .first()

    def updateStudent(self, student_id, name):
        student = self.getStudent(student_id)
        student.name = name
        self.session.commit()

    def deleteStudent(self, student_id):
        student = self.getStudent(student_id)
        self.session.delete(student)
        self.session.commit()

    def registerStudentFace(self, student_id, face_embedding):
        face = Face(student_id=student_id, face_embedding=face_embedding)
        self.session.add(face)
        self.session.commit()

    def getStudentFromFace(self, face_embedding):
        face = self.session.query(Face)\
            .filter(Face.face_embedding.distance(face_embedding) < 0.6)\
            .first()
        return self.session.query(Student)\
            .filter(Student.id == face.student_id)\
            .first()

