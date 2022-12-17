import cv2
import humanposemodule as hpm

from tkinter import *
from PIL import ImageTk, Image


def exit_app():
    global isOpened
    isOpened = False


isOpened = True

cap = cv2.VideoCapture(0)

previous_time = 0
current_time = 0

img0 = cv2.imread("images/0.png")
img1 = cv2.imread("images/1.png")
img2 = cv2.imread("images/2.png")
img3 = cv2.imread("images/3.png")

posedetect = hpm.PoseDetector(detection_confident=0.8)

win = Tk()
win.title("Traffic controller")
win.resizable(False, False)
win.configure(bg="white")

check, frame = cap.read()
if check:
    canvas = Canvas(win, width=640, height=640, background="white")
    canvas.pack()
    Button(win, text="Exit", command=exit_app, width=10, height=2).pack()

while isOpened:
    win.update_idletasks()
    win.update()

    check, frame = cap.read()

    if check:

        frame = cv2.resize(frame, (645, 400))
        frame = posedetect.find_pose(frame, draw_landmark=True)
        lmlist = posedetect.find_location(frame, draw_landmark=True)

        situation_id = 0

        if len(lmlist) != 0:
            rotation = posedetect.find_rotation()
            if rotation == "back":
                situation_id = 0
            elif rotation == "front":
                if posedetect.find_dist(12, 16) < 0.4 * posedetect.find_dist(12, 24):
                    situation_id = 1
                else:
                    situation_id = 0
            elif rotation == "right_side":
                if posedetect.find_angle(24, 12, 16) > 70:

                    situation_id = 0
                else:
                    situation_id = 2
            elif rotation == "left_side":
                if posedetect.find_angle(24, 12, 16) > 70:
                    situation_id = 3
                else:
                    situation_id = 2

        if situation_id == 0:
            img = img0

        elif situation_id == 1:
            img = img1

        elif situation_id == 2:
            img = img2

        elif situation_id == 3:
            img = img3
        else:
            img = img0

        img = cv2.resize(img, (300, 200))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        frametk = ImageTk.PhotoImage(image=Image.fromarray(frame))
        imgtk = ImageTk.PhotoImage(image=Image.fromarray(img))

        canvas.create_image(320, 200, anchor=CENTER, image=frametk)
        canvas.create_image(320, 520, anchor=CENTER, image=imgtk)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
win.destroy()
