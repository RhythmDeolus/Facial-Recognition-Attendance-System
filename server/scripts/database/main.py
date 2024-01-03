import psycopg2
import face_recognition as fr
from DatabaseAPI import DatabaseAPI

conn = psycopg2.connect(database="attendance_system",
                        host="localhost",
                        user="admin",
                        password="1234",
                        port="5432")


face_recog = DatabaseAPI(conn)

image1 = fr.load_image_file('R.jpg')
image2 = fr.load_image_file('M.jpg')

print(face_recog.deleteStudent(2))
print(face_recog.getStudentID(image2))
