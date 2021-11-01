import cv2 as cv

img1 = cv.imread("../assets/image_1.png")
img2 = cv.imread("../assets/image_2.png")
img_template = img1[100:150, 100:150].copy()

res = cv.matchTemplate(img1, img_template, cv.TM_CCOEFF_NORMED)
max_loc = cv.minMaxLoc(res)[3]
top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv.rectangle(img1, top_left, bottom_right, 255, 2)

res = cv.matchTemplate(img2, img_template, cv.TM_CCOEFF_NORMED)
max_loc = cv.minMaxLoc(res)[3]
top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv.rectangle(img2, top_left, bottom_right, 255, 2)

cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.imshow("res", res)
cv.imshow("img_template", img_template)

cv.waitKey(0)
cv.destroyAllWindows()
