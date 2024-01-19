import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

cap = cv2.VideoCapture(0)

bottleColor = [163, 150, 8]
yellow = [0, 255, 255]
def colorlimits(color):
      
      x = np.uint8([[color]])
      hsvX = cv2.cvtColor(x, cv2.COLOR_BGR2HSV)
      
      lowerLim = hsvX[0][0][0] - 10, 100, 100
      upperLim = hsvX[0][0][0] - 10, 255, 255

      lowerLim = np.array(lowerLim, dtype = np.uint8)
      upperLim = np.array(upperLim, dtype = np.uint8)

      return lowerLim, upperLim

while True:
        ret, frame = cap.read()

        hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lowerLim, upperLim = colorlimits(color = yellow)
        
        mask = cv2.inRange(hsvImg, lowerLim, upperLim)

      #BOUNDING BOX
        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()

        if bbox is not None:
               x1, y1, x2, y2 = bbox

               frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

        #print(bbox)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
                break
cap.release()

