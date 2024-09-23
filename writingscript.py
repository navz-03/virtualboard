import cv2
import numpy as np
import time
import os
import handtrackingfile as htf

overlaylist = []
brushthicknes = 10
eraserthicknes = 100
drawcolour = (0, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htf.handdectector(detectionCon=0.85)
xp, yp = 0, 0
imgcanvas = np.zeros((720, 1280, 3),np.uint8)

while True:
    # import video
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findhands(img)
    lmlist = detector.findpostion(img, draw=False)

    if len(lmlist) != 0:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        fingers = detector.fingersup()
        #print(fingers)
        # if selection mode -two fingers up
        if fingers[1] and fingers[2]:
          xp, yp = 0, 0
          cv2.rectangle(img, (x1, y1 - 15), (x2, y2 + 15), drawcolour, cv2.FILLED)
          print("selection mode")
          if y1 < 125:
              #if 250 < 450:
                  #header = overlaylist[0]
              if 750 < x1 < 850:
                  header = overlaylist[0]
                  drawcolour = (0, 0, 255)
              elif 900 < x1 < 1000:
                  header = overlaylist[1]
                  drawcolour = (255, 0, 0)
              elif 1050 < x1 < 1200:
                  header = overlaylist[2]
                  drawcolour = (0, 0, 0)
          cv2.rectangle(img, (x1, y1 - 15), (x2, y2 + 15), drawcolour, cv2.FILLED)
        # drawing mode - one finger up
        if fingers[1] and fingers[2]==False:
          cv2.circle(img, (x1,y1), 15, drawcolour, cv2.FILLED)
          print("Drawing mode")
          if xp == 0 and yp == 0:
              xp, yp = x1, y1

          if drawcolour == (0,0,0):
              cv2.line(img, (xp, yp), (x1, y1), drawcolour, eraserthicknes)
              cv2.line(imgcanvas, (xp, yp), (x1, y1), drawcolour, eraserthicknes)
          else:
            cv2.line(img, (xp, yp), (x1, y1), drawcolour, brushthicknes)
            cv2.line(imgcanvas, (xp, yp), (x1, y1), drawcolour, brushthicknes)
          xp, yp = x1, y1

    #imggray = cv2.cvtColor(imgcanvas, cv2.COLOR_BGR2RGB)
    #_, cv2.threshold(imggray, 50, 255, cv2.THRESH_BINARY_INV)
    #imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    #img=cv2.bitwise_and(img,imgInv)
    #img=cv2.bitwise_or(img,imgcanvas)

    # importimage
    img = cv2.addWeighted(img, 0.5, imgcanvas, 0.5, 0)
    #cv2.imshow("video", img)
    cv2.imshow("canvas", imgcanvas)
    cv2.waitKey(1)