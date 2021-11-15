import cv2

face_cascade = cv2.CascadeClassifier(
    '../assets/cascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    '../assets/cascade/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('../assets/cascade/mouth.xml')
cap = cv2.VideoCapture(0)

# while True:
#     _, frame = cap.read()
frame = cv2.imread("../assets/face.png")
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 4)
eye = eye_cascade.detectMultiScale(gray, 1.3, 4)
mouth = mouth_cascade.detectMultiScale(gray, 1.3, 4)

biggest_object = [0, 0, 0, 0]
for (x, y, w, h) in faces:
    if biggest_object[2] < w:
        biggest_object = [x, y, w, h]
cv2.putText(frame, "face", (biggest_object[0], biggest_object[1]),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
cv2.rectangle(frame, (biggest_object[0], biggest_object[1]), (
    biggest_object[0]+biggest_object[2], biggest_object[1]+biggest_object[3]), (255, 0, 0), 2)

biggest_object = [0, 0, 0, 0]
for (x, y, w, h) in eye:
    if biggest_object[2] < w:
        biggest_object = [x, y, w, h]
cv2.putText(frame, "eye", (biggest_object[0], biggest_object[1]),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
cv2.rectangle(frame, (biggest_object[0], biggest_object[1]), (
    biggest_object[0]+biggest_object[2], biggest_object[1]+biggest_object[3]), (0, 255, 0), 2)

biggest_object = [0, 0, 0, 0]
for (x, y, w, h) in mouth:
    if biggest_object[2] < w:
        biggest_object = [x, y, w, h]
cv2.putText(frame, "mouth", (biggest_object[0], biggest_object[1]),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.rectangle(frame, (biggest_object[0], biggest_object[1]), (
    biggest_object[0]+biggest_object[2], biggest_object[1]+biggest_object[3]), (0, 0, 255), 2)

cv2.imshow('img', frame)
k = cv2.waitKey(0)
# if k == 27:
#     break

cv2.destroyAllWindows()
