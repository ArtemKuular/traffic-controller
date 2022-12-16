import cv2
import mediapipe as mp
import math


class PoseDetector:
    def __init__(self, static_mode=False, model_complexity=1, upbbody=False, smooth=True, detection_confident=0.5,
                 tracking_confident=0.5):
        self.lmlist = None
        self.results = None
        self.static_mode = static_mode
        self.complexity = model_complexity
        self.upbbody = upbbody
        self.smooth = smooth
        self.detection_confident = detection_confident
        self.tracking_confident = tracking_confident

        self.mppose = mp.solutions.pose
        self.pose = self.mppose.Pose(self.static_mode, self.complexity, self.upbbody, self.smooth,
                                     self.detection_confident,
                                     self.tracking_confident)
        self.mpdraw = mp.solutions.drawing_utils

    def find_pose(self, frame, draw_landmark=True):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img)

        if self.results.pose_landmarks:
            if draw_landmark:
                self.mpdraw.draw_landmarks(frame, self.results.pose_landmarks, self.mppose.POSE_CONNECTIONS)

    def find_location(self, frame, draw_landmark=True):
        self.lmlist = []
        if self.results.pose_landmarks:
            mypose = self.results.pose_landmarks

            for idx, lm in enumerate(mypose.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                self.lmlist.append([idx, cx, cy])
                if draw_landmark:
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        return self.lmlist

    def find_angle(self, p1, p2, p3):
        pass

    def find_rotation(self):
        x1, y1 = self.lmlist[11][1:]
        x2, y2 = self.lmlist[12][1:]
        if x2 > x1:
            return "back"
        else:
            return 'front'

