import cv2

img = cv2.imread("lena.png")

top, left = 338, 282
h, w = 216, 106

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
crop_img = cv2.rectangle(img, (left, top), (left+w, top+h), (0, 255, 0), 3)

retval, thresh = cv2.threshold(gray_img, 127, 255, 0)
img_contours, _ = cv2.findContours(
    thresh[top:top+h, left:left+w], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img[top:top+h, left:left+w], img_contours, -1, (255, 0, 0))

cv2.imshow("test", img)
cv2.waitKey(0)
