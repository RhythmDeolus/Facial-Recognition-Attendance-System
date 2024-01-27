from fastapi import FastAPI, responses
from fastapi.staticfiles import StaticFiles
from scripts.api1 import api1
import uvicorn

import psycopg2
from scripts.database.DatabaseAPI import DatabaseAPI
app = FastAPI()

api1.conn = None

api1.database = None


@app.on_event('startup')
async def startup_event():
    api1.conn = psycopg2.connect(database="attendance_system",
                                 host="localhost",
                                 user="admin",
                                 password="1234",
                                 port="5432")
    print("connection established: ", api1.conn)
    api1.database = DatabaseAPI(api1.conn)
    print("api established: ", api1.database)


# app.mount("/static/", StaticFiles(directory="client/dist/static"), name="static")
app.mount("/api_1", api1)
app.mount("/", StaticFiles(directory="client/dist", html=True), name="static")

@app.exception_handler(404)
async def custom_404_handler(_, __):
        return  responses.FileResponse('./client/dist/index.html')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
