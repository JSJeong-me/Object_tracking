import sys
import numpy as np
import cv2

frame = cv2.imread('032.png')

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


# Banana Grade
low_yello = np.array([0, 0, 0]) # 8,159,195   223, 193, 62
high_yello = np.array([255, 255, 250])
#high_yello = np.array([230, 230, 250]) # 120,225,248  247, 222, 91
banana_mask = cv2.inRange(hsv_frame, low_yello, high_yello)
banana = cv2.bitwise_and(frame, frame, mask=banana_mask)


cv2.imshow('Image', frame)
#cv2.imshow('Blue mask', blue)
#cv2.imshow('Red mask', red)
#cv2.imshow('Green mask', green)
cv2.imshow('Banana mask', banana)
#cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()