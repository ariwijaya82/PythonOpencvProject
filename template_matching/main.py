import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

cam = cv2.VideoCapture(0)

left_eye = cv2.imread('../left_eye.png')
right_eye = cv2.imread('../right_eye.png')
h1, w1 = left_eye.shape[:2]
h2, w2 = right_eye.shape[:2]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

while True:
    ret, frame = cam.read()

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(frame, left_eye, cv2.TM_CCOEFF_NORMED)
    max_loc = cv2.minMaxLoc(res)[3]
    top_left = max_loc
    bottom_right = (top_left[0] + w1, top_left[1] + h1)
    cv2.rectangle(frame, top_left, bottom_right, 255, 2)
    cv2.putText(frame, "left eye", (top_left[0], top_left[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    pos1 = top_left

    res = cv2.matchTemplate(frame, right_eye, cv2.TM_CCOEFF_NORMED)
    max_loc = cv2.minMaxLoc(res)[3]
    top_left = max_loc
    bottom_right = (top_left[0] + w1, top_left[1] + h1)
    cv2.rectangle(frame, top_left, bottom_right, 255, 2)
    cv2.putText(frame, "right eye", (top_left[0], top_left[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    pos2 = top_left

    print("r_x:", abs(pos1[0]-pos2[0]), "r_y:", abs(pos1[1]-pos2[1]))

    cv2.imshow('result', frame)

    if cv2.waitKey(10) == 27:
        break
