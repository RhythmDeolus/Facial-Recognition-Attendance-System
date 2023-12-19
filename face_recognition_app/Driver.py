from Camera import Camera
from Display import Display
from FaceRecog import FaceRecog
import face_recognition

import threading
import queue

import tracemalloc
import time

import requests

tracemalloc.start()

c = Camera()

f = FaceRecog()

c.open()

d = Display(0, 'Main Window')

i = 0
n = 10

q = queue.Queue()

cache = {
  'index': [],
  'value': []
}


def mark_attendance(url, json):
    response = requests.post(url, json=json)
    if response.status_code == 200:
        return response.json()
    else:
        print('invalid response')
    return {}


def worker():
    url = 'http://127.0.0.1:5000/api/markAttendance'
    while True:
        image = q.get()
        frame = f.resizeImg(image, 0.25)
        faces = f.detectFaces(frame)
        encodings = f.getEncodings(frame, faces)
        for encoding in encodings:
            matches = face_recognition.compare_faces(cache['index'],
                                                     encoding, tolerance=0.6)
            try:
                matches.index(True)
            except Exception:
                res = mark_attendance(url,
                                      {'encoding': encoding.tolist(),
                                       'time': time.time()})
                if ('id' in res):
                    print('Attendance was marked for student id: ', res['id'])
                    cache['index'].append(encoding)
                    cache['value'].append(res['id'])
        q.task_done()


threading.Thread(target=worker, daemon=True).start()

while True:
    time.sleep(0.16)
    frame1 = c.get_image()
    if i % n == 0:
        i = 0
        if q.empty():
            q.put(frame1, False)
    d.displayimg(frame1)
    i += 1
