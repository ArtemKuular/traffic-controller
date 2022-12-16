import numpy as np
import cv2
import mediapipe as mp
import time
import humanposemodule as hpm

cap = cv2.VideoCapture(0)

previous_time = 0
current_time = 0

img0 = cv2.imread("images/0.png")
img1 = cv2.imread("images/1.png")
img2 = cv2.imread("images/2.png")
img3 = cv2.imread("images/3.png")

posedetect = hpm.PoseDetector(detection_confident=0.8)

while True:

    check, frame = cap.read()

    if check:

        frame = cv2.resize(frame, (1280, 720))
        frame = posedetect.find_pose(frame, draw_landmark=True)
        lmlist = posedetect.find_location(frame, draw_landmark=True)

        situation_id = 0

        if len(lmlist) != 0:
            rotation = posedetect.find_rotation()
            if rotation == "back":
                pass
            elif rotation == "front":
                pass
            elif rotation == "right_side":
                pass
            elif rotation == "left_side":
                pass

        if situation_id == 0:
            img = img0

        elif situation_id == 1:
            img = img1

        elif situation_id == 2:
            img = img2

        elif situation_id == 3:
            img = img3

        img = cv2.resize(img, (frame.shape[1], int(frame.shape[0])))
        frame = np.concatenate((frame, img), axis=0)

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(frame, "frame rate: " + str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 255), 5)

        cv2.imshow('Traffic controller', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
