import cv2
import numpy as np
import imutils


def callback(x):
    pass


cap = cv2.VideoCapture(2)
cv2.namedWindow('image')

ilowH = 8
ihighH = 35
ilowS = 29
ihighS = 255
ilowV = 174
ihighV = 255

# create trackbars for color change
# cv2.createTrackbar('lowH', 'image', 0, 255, callback)
# cv2.createTrackbar('highH', 'image', 0, 255, callback)

# cv2.createTrackbar('lowS', 'image', 0, 255, callback)
# cv2.createTrackbar('highS', 'image', 0, 255, callback)

# cv2.createTrackbar('lowV', 'image', 0, 255, callback)
# cv2.createTrackbar('highV', 'image', 0, 255, callback)


while True:
    # grab the frame
    ret, frame = cap.read()

    # get trackbar positions
    # ilowH = 8 #cv2.getTrackbarPos('lowH', 'image')
    # ihighH = 35 #cv2.getTrackbarPos('highH', 'image')
    # ilowS = 29 #cv2.getTrackbarPos('lowS', 'image')
    # ihighS = 255 #cv2.getTrackbarPos('highS', 'image')
    # ilowV = 174 #cv2.getTrackbarPos('lowV', 'image')
    # ihighV = 255 #cv2.getTrackbarPos('highV', 'image')

    frame = imutils.resize(frame, width=600)
    blured = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        cv2.putText(frame, "center position: " + str(center), (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    # frame = cv2.bitwise_and(frame, frame, mask=mask)

    # show thresholded image
    cv2.imshow('image', frame)
    k = cv2.waitKey(1) & 0xFF  # large wait time to remove freezing
    if k == 113 or k == 27:
        break


cv2.destroyAllWindows()
cap.release()
