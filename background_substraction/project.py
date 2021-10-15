import cv2 as cv
import numpy as np

# background substruction initialize
backSub = cv.createBackgroundSubtractorMOG2(detectShadows=False)
backSub.setBackgroundRatio(2)
backSub.setVarThreshold(150)

# get video
capture = cv.VideoCapture("videojalan.mp4")

# set area point where car detected
p1 = (280, 170)
p2 = (180, 320)
p3 = (320, 340)
p4 = (360, 180)
contours = np.array([p1, p2, p3, p4])

# exit program when failed open video
if not capture.isOpened():
    print("Unable to open camera")
    exit(0)

# global variable
count = 0
car = False
connected_component_thresh = 10

# main loop
while True:

    # get frame from video
    ret, frame = capture.read()
    if frame is None:
        break

    # apply background substruction
    fgMask = backSub.apply(frame)

    # apply bitwise to roi
    tmp = np.zeros(shape=fgMask.shape, dtype=fgMask.dtype)
    cv.fillPoly(tmp, pts=[contours], color=(255, 255, 255))
    bitwise_image = cv.bitwise_and(fgMask, tmp)

    # count car with connected component
    ret, labels = cv.connectedComponents(bitwise_image)
    if not car and ret > connected_component_thresh:
        count += 1

    if ret > connected_component_thresh:
        car = True
    elif ret <= connected_component_thresh:
        car = False

    # show count car value
    cv.putText(frame, "count car: " + str(count), (10, 100),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv.imshow("original", frame)
    cv.imshow("back_subs", fgMask)
    cv.imshow("bitwise", bitwise_image)

    keyboard = cv.waitKey(30)
    if keyboard == 27:
        break

cv.destroyAllWindows()
