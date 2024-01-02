from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from scripts.api1 import api1

import psycopg2
from database.DatabaseAPI import DatabaseAPI
app = FastAPI()

api1.conn = None

api1.face_recog = None

@app.on_event('startup')
async def startup_event():
    api1.conn = psycopg2.connect(database="attendance_system",
                            host="localhost",
                            user="admin",
                            password="1234",
                            port="5432")
    print("connection established: ", api1.conn)
    api1.face_recog = DatabaseAPI(api1.conn)
    print("api established: ", api1.face_recog)


app.mount("/static/", StaticFiles(directory="dist/static"), name="static")
app.mount("/api_1", api1)
app.mount("/", StaticFiles(directory="dist", html=True), name="static")
