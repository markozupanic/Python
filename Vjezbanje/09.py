import numpy as np
import cv2

cap = cv2.VideoCapture(0)
foreground_background = cv2.createBackgroundSubtractorKNN()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    foreground_mask = foreground_background.apply(frame)
    cv2.imshow('Output', foreground_mask)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
