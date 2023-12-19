import face_recognition
import cv2
import numpy as np
import threading


class FaceRecog(threading.Thread):
    def resizeImg(self, image, frac):
        return cv2.resize(image, (0, 0), fx=frac, fy=frac)

    def detectFaces(self, image):
        image = np.ascontiguousarray(image[:, :, ::-1])
        return face_recognition.face_locations(image)

    def getEncodings(self, image, face_locations):
        return face_recognition.face_encodings(image, face_locations)
