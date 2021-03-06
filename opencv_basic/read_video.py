import cv2 as cv

cap = cv.VideoCapture(2)
if not cap.isOpened():
    print("connot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("cant recieve frame (stream end?). Exiting...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
