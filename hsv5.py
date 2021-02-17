import sys
import numpy as np
import cv2

frame = cv2.imread('078.png')

hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Every color except white & Green
low = np.array([15, 52, 72]) #  0, 42, 0 - white
high = np.array([179, 255, 255])
mask = cv2.inRange(hsv_frame, low, high)
result = cv2.bitwise_and(frame, frame, mask=mask)


# Banana Grade
low_yello = np.array([0, 80, 70]) # 8,159,195   223, 193, 62
high_yello = np.array([255, 255, 255])
#high_yello = np.array([230, 230, 250]) # 120,225,248  247, 222, 91
banana_mask = cv2.inRange(hsv_frame, low_yello, high_yello)
banana = cv2.bitwise_and(frame, frame, mask=banana_mask)


cv2.imshow('Image', frame)
#cv2.imshow('Banana mask', banana)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()