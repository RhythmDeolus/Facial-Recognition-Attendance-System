from fastapi import FastAPI, responses
from fastapi.staticfiles import StaticFiles
from scripts.api.v2.api import api
import uvicorn
import os
from dotenv import load_dotenv
import psycopg2
from scripts.database.DatabaseAPI import DatabaseAPI
load_dotenv()

app = FastAPI()

api.conn = None

api.database = None


@app.on_event('startup')
async def startup_event():
    api.conn = psycopg2.connect(os.getenv('DB_URL'))
    print("connection established: ", api.conn)
    api.database = DatabaseAPI(api.conn)
    print("api established: ", api.database)


# app.mount("/static/", StaticFiles(directory="client/dist/static"), name="static")
app.mount("/api_1", api)
app.mount("/", StaticFiles(directory="client/dist", html=True), name="static")

@app.exception_handler(404)
async def custom_404_handler(_, __):
    return responses.FileResponse('./client/dist/index.html')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
