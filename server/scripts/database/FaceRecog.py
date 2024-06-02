import face_recognition
import cv2
import numpy as np
import threading
import base64
from PIL import Image
import io


class FaceRecog(threading.Thread):
    def stringToArray(self, base64_string):
        imgdata = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(imgdata))
        image = image.convert('RGB')
        arr = np.array(image)
        arr = cv2.flip(arr, 1)
        return arr

    def resizeImg(self, image, frac):
        return cv2.resize(image, (0, 0), fx=frac, fy=frac)

    def detectFaces(self, image):
        image = np.ascontiguousarray(image[:, :, ::-1])
        return face_recognition.face_locations(image)

    def getEncodings(self, image, face_locations):
        return face_recognition.face_encodings(image, face_locations)
