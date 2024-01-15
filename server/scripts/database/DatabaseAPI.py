from pgvector.psycopg2 import register_vector
import face_recognition as fr
import numpy as np
from datetime import datetime
from functools import wraps

def handle_error(value=None):
    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                print(e)
                args[0].conn.rollback()
                return value
        return inner
    return outer

class DatabaseAPI:
    def __init__(self, conn):
        self.conn = conn
        self.createDatabase()
        register_vector(conn)
    
    @handle_error()
    def createDatabase(self):
        cursor = self.conn.cursor()
        cursor.execute("""CREATE EXTENSION IF NOT EXISTS vector;
            CREATE TABLE IF NOT EXISTS student (
                id int PRIMARY KEY,
                name varchar(20) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS face_id (
                student_id int REFERENCES student(id),
                face_embedding vector(128)
            );
            CREATE TABLE IF NOT EXISTS attendance (
                attendance_id bigserial PRIMARY KEY,
                student_id int REFERENCES student(id),
                time timestamp NOT NULL,
                tdate date GENERATED ALWAYS AS (date(time)) STORED
            );
            ALTER TABLE attendance DROP CONSTRAINT IF EXISTS check_attendance;
            ALTER TABLE attendance ADD CONSTRAINT check_attendance UNIQUE(student_id, tdate);
        """)
        self.conn.commit()

    @handle_error()
    def getStudentID(self, embedding: list[float]) -> int | None:
            cursor = self.conn.cursor()
            embedding = np.array(embedding)
            cursor.execute('SELECT student_id, face_embedding FROM face_id ORDER BY face_embedding <=> %s LIMIT 5;', (embedding, ))
            for record in cursor:
                if fr.compare_faces([record[1]], embedding, tolerance=0.6)[0]:
                    return record
            return None

    @handle_error(False)
    def registerStudent(self, embedding: list[float], studentID: int) -> bool:
        cursor = self.conn.cursor()
        embedding = np.array(embedding)
        cursor.execute('INSERT INTO face_id (student_id, face_embedding) VALUES %s;', ((studentID, embedding),))
        self.conn.commit()
        return True

    @handle_error(False)
    def deleteStudent(self, studentID: int) -> bool:
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM face_id WHERE student_id = %s;', (studentID,))
        self.conn.commit()
        return True

    @handle_error(False)
    def update_embedding(self, student_id: int, embedding: list[float]) -> bool:
        cursor = self.conn.cursor()
        embedding = np.array(embedding)
        cursor.execute('UPDATE face_id SET face_embedding = %s WHERE student_id = %s;', (embedding, student_id,))
        self.conn.commit()
        return True
        
    @handle_error([])
    def get_attendance(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM attendance;')
        response = cursor.fetchall()
        return response

    @handle_error([])
    def get_students(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM student;')
        response = cursor.fetchall()
        return response


    @handle_error(False)
    def mark_attendance(self, student_id: int, time: datetime) -> bool:
        print('marked attendance for: ', student_id)
        print('at time: ', time)
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO attendance (student_id, time) VALUES %s;', ((student_id, time),))
        self.conn.commit()
        return True
