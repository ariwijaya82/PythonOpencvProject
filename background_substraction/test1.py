import cv2 as cv
import numpy as np

p1 = (280, 170)
p2 = (180, 320)
p3 = (320, 340)
p4 = (360, 180)
contours = np.array([p1, p2, p3, p4])

tmp = np.zeros((500, 500))
cv.fillPoly(tmp, pts=[contours], color=(255, 255, 255))

cv.imshow("test", tmp)
cv.waitKey(0)
