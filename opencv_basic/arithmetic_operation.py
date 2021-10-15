import cv2 as cv

img1 = cv.imread("messi.jpg")
img2 = cv.imread("lena.png")

rows, cols, channels = img1.shape
roi = img2[0:rows, 0:cols]

img1gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img1gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

img2_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
img1_bg = cv.bitwise_and(img1, img1, mask=mask)
cv.imshow("img2_bg", img1_bg)

dst = cv.add(img1_bg, img2_bg)
img2[0:rows, 0:cols] = dst

cv.imshow('res', img2)
cv.waitKey(0)
cv.destroyAllWindows()
