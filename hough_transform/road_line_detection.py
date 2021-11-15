# created by: I Made Pande Ari Wijaya (07111740000020)

import cv2
import numpy as np

video = cv2.VideoCapture("../assets/road.mp4")

# akses video
while(True):
    ret, orig_frame = video.read()
    gray = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    ret, thresh = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY)  # threshold
    # transform morfologi
    dilated = cv2.dilate(thresh, cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (4, 8)), iterations=3)
    erode = cv2.erode(dilated, cv2.getStructuringElement(
        cv2.MORPH_RECT, (2, 4)), iterations=3)

    edges = cv2.Canny(erode, threshold1=50, threshold2=50)

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, None, 50, 10)
    if lines is not None:
        for line in range(0, len(lines)):
            l = lines[line][0]
            cv2.line(orig_frame, (l[0], l[1]),
                     (l[2], l[3]), (0, 0, 255), 3, cv2.LINE_AA)

    cv2.imshow('erode', erode)
    cv2.imshow("frame", edges)
    cv2.imshow("edges", orig_frame)

    if cv2.waitKey(1) > 0:
        break

video.release()
cv2.destroyAllWindows()
