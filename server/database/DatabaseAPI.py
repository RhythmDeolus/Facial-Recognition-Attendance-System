from pgvector.psycopg2 import register_vector
import face_recognition as fr
import numpy as np
from datetime import datetime


class DatabaseAPI:
    def __init__(self, conn):
        self.conn = conn
        register_vector(conn)

    def getStudentID(self, embedding: list[float]) -> int | None:
        cursor = self.conn.cursor()
        embedding = np.array(embedding)
        cursor.execute('SELECT student_id, face_embedding FROM face_id ORDER BY face_embedding <=> %s LIMIT 5;', (embedding, ))
        for record in cursor:
            if fr.compare_faces([record[1]], embedding, tolerance=0.6)[0]:
                return record[0]
        return None

    def registerStudent(self, embedding: list[float], studentID: int) -> bool:
        cursor = self.conn.cursor()
        embedding = np.array(embedding)
        try:
            cursor.execute('INSERT INTO face_id (student_id, face_embedding) VALUES %s;', ((studentID, embedding),))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def deleteStudent(self, studentID: int) -> bool:
        cursor = self.conn.cursor()
        try:
            cursor.execute('DELETE FROM face_id WHERE student_id = %s;', (studentID,))
            self.conn.commit()
            return True
        except Exception:
            return False

    def update_embedding(self, student_id: int, embedding: list[float]) -> bool:
        cursor = self.conn.cursor()
        embedding = np.array(embedding)
        try:
            cursor.execute('UPDATE face_id SET face_embedding = %s WHERE student_id = %s;', (embedding, student_id,))
            self.conn.commit()
            return True
        except Exception:
            return False

    def mark_attendance(self, student_id: int, time: datetime) -> bool:
        print('marked attendance for: ', student_id)
        print('at time: ', time)
        return True
