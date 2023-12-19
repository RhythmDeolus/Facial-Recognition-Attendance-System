from threading import Thread, Lock
import cv2
import numpy

class Display (Thread):
  def __init__(self, threadId, name):
    Thread.__init__(self)
    self.threadId = threadId
    self.name = name
    self.img = None
    self.setDaemon(True)
    self.start()
    
  def run(self):
    while True:
      if type(self.img) is numpy.ndarray:
        cv2.imshow("attendance system", self.img)
        cv2.waitKey(83)

  def displayimg(self, img):
    del self.img
    self.img = img