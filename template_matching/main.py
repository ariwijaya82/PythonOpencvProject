# created by: I Made Pande Ari Wijaya (07111740000020)
import cv2

cam = cv2.VideoCapture(0)

left_eye = cv2.imread('../left_eye.png')
right_eye = cv2.imread('../right_eye.png')
h1, w1 = left_eye.shape[:2]
h2, w2 = right_eye.shape[:2]

while True:
    ret, frame = cam.read()

    # template matcing for left eye
    res = cv2.matchTemplate(frame, left_eye, cv2.TM_CCOEFF_NORMED)
    max_loc = cv2.minMaxLoc(res)[3]
    top_left = max_loc
    bottom_right = (top_left[0] + w1, top_left[1] + h1)
    # make marker for left eye matching
    cv2.rectangle(frame, top_left, bottom_right, 255, 2)
    cv2.putText(frame, "left eye", (top_left[0], top_left[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    # save position of left eye matching
    pos1 = top_left

    # template matcing for right eye
    res = cv2.matchTemplate(frame, right_eye, cv2.TM_CCOEFF_NORMED)
    max_loc = cv2.minMaxLoc(res)[3]
    top_left = max_loc
    bottom_right = (top_left[0] + w1, top_left[1] + h1)
    # make marker for right eye matching
    cv2.rectangle(frame, top_left, bottom_right, 255, 2)
    cv2.putText(frame, "right eye", (top_left[0], top_left[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    # save position of right eye matching
    pos2 = top_left

    # print each eye position
    print("r_x:", abs(pos1[0]-pos2[0]), "r_y:", abs(pos1[1]-pos2[1]))
    # calculate pixel distance between eyes
    x = abs(pos1[0]-pos2[0])
    # calculate distance face from camera with linear regression
    dist = -1.4600*x + 193.4000
    cv2.putText(frame, "Jarak: " + str(dist), (frame.shape[0] // 4, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('result', frame)

    if cv2.waitKey(10) == 27:
        break
