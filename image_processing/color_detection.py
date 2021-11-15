import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cv.namedWindow('image')


def nothing(x):
    pass


while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    cv.createTrackbar('lower_h', 'image', 0, 360, nothing)
    cv.createTrackbar('upper_h', 'image', 0, 360, nothing)
    cv.createTrackbar('lower_s', 'image', 0, 100, nothing)
    cv.createTrackbar('upper_s', 'image', 0, 100, nothing)
    cv.createTrackbar('lower_v', 'image', 0, 100, nothing)
    cv.createTrackbar('upper_v', 'image', 0, 100, nothing)

    upper_h = cv.getTrackbarPos('upper_h', 'image')
    upper_s = cv.getTrackbarPos('upper_s', 'image')
    upper_v = cv.getTrackbarPos('upper_v', 'image')

    lower_h = cv.getTrackbarPos('lower_h', 'image')
    lower_s = cv.getTrackbarPos('lower_s', 'image')
    lower_v = cv.getTrackbarPos('lower_v', 'image')

    upper = [upper_h, upper_s, upper_v]
    lower = [lower_h, lower_s, lower_v]

    mask = cv.inRange(hsv, lower, upper)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('original', frame)
    cv.imshow('image', mask)
    cv.imshow('result', res)
    k = cv.waitKey(5)
    if k == 27:
        break

cv.destroyAllWindows()
