import cv2 as cv
import sys

img = cv.imread("../assets/lena.png", cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == 27:
    exit(0)
