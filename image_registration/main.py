import cv2 as cv

img1 = cv.imread("../assets/image_1.png")
img2 = cv.imread("../assets/image_2.png")
h, w, c = img2.shape
loc1 = ()
loc2 = ()

for i in range(0, h, 100):
    for j in range(0, w, 100):
        template = img1[i:i+100, j:j+100].copy()
        temp_match = cv.matchTemplate(img2, template, cv.TM_CCOEFF_NORMED)
        max_loc = cv.minMaxLoc(temp_match)[3]
        max_val = cv.minMaxLoc(temp_match)[1]
        cv.rectangle(img1, (j, i), (j+100, i+100), 255, 2)
        if max_val > 0.9:
            cv.rectangle(
                img2, max_loc, (max_loc[0]+100, max_loc[1]+100), 255, 2)
            loc2

        cv.imshow("img1", img1)
        cv.imshow("img2", img2)
        cv.imshow("template", template)
        cv.waitKey(0)

# img_template = img1[100:150, 100:150].copy()

# res = cv.matchTemplate(img1, img_template, cv.TM_CCOEFF_NORMED)
# max_loc = cv.minMaxLoc(res)[3]
# top_left = max_loc
# bottom_right = (top_left[0] + 50, top_left[1] + 50)
# cv.rectangle(img1, top_left, bottom_right, 255, 2)

# res = cv.matchTemplate(img2, img_template, cv.TM_CCOEFF_NORMED)
# max_loc = cv.minMaxLoc(res)[3]
# top_left = max_loc
# bottom_right = (top_left[0] + 50, top_left[1] + 50)
# cv.rectangle(img2, top_left, bottom_right, 255, 2)

# cv.imshow("img1", img1)
# cv.imshow("img2", img2)
# cv.imshow("res", res)
# cv.imshow("img_template", img_template)

# cv.waitKey(0)
cv.destroyAllWindows()
