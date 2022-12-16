import cv2
import mediapipe as mp
import time
import math


class PoseDetector:
    def __init__(self, static_mode=False, model_complexity=1, upbbody=False, smooth=True, detection_confident=0.5,
                 tracking_confident=0.5):
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
        pass

    def find_location(self, frame, draw_landmark=True):
        pass

    def find_angle(self, p1, p2, p3):
        pass

    def find_rotation(self):
        pass

