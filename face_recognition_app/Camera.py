import cv2

class Camera:
  def __init__(self):
    self.vid = None

  def open(self):

    self.vid = cv2.VideoCapture(0)

  def get_image(self):
    _ , frame = self.vid.read()

    frame = cv2.flip(frame, 1)

    # b, g, r = cv2.split(frame)
    # frame = cv2.merge((r, g, b))

    return frame
  def close(self):
    self.vid.release()

