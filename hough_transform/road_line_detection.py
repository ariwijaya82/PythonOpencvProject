import cv2
import numpy as np

video = cv2.VideoCapture("../assets/road.mp4")

while True:
    ret, orig_frame = video.read()
