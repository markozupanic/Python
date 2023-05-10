import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_yellow = np.array([90,50,50]) 
upper_yellow = np.array([120,255,255])
#Loop until break statement is exectured 
while True:
    ret, frame = cap.read()
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('original', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('Filtered Color Only', res)
    if cv2.waitKey(1) == 13: 
        break
cap.release() 
cv2.destroyAllWindows()