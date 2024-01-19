"""
Authors: Alan Berg, Tomasz Fidurski

This Python script includes functionality for face and eye detection using OpenCV,
GUI automation with pyautogui, GUI creation using tkinter, and multimedia handling with pygame.
It utilizes Haar cascade classifiers for detecting facial features in real-time video feed.
"""

import cv2
import pyautogui
import tkinter as tk
import webbrowser
import time
import pygame
from PIL import Image, ImageTk

""" Initialize pygame mixer """
pygame.mixer.init()

""" Load face and eye cascade classifiers """
faceCascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("cascade/haarcascade_eye.xml")

""" Variables to track consecutive eye states and set thresholds """
cap = cv2.VideoCapture(0)

""" Counter to track consecutive closed eyes """
consecutive_closed_eyes = 0
consecutive_open_eyes = 0
threshold_closed_eyes = 3
threshold_open_eyes = 7

youtube_video_url = "https://youtu.be/BEo-XBIc0qA?si=lm2_vT8ZNXPWVTqh"
webbrowser.open(youtube_video_url, new=2)

""" Film status flag """
film_status = "running"

""" Variable to track the time when the video was paused """
paused_time = None

""" Create the main window """
root = tk.Tk()
root.title("Face Recognition")

""" Create frame for video display """
video_frame = tk.Label(root)
video_frame.pack()

""" Status label to display film status """
status_label = tk.Label(root, text="", font=("Helvetica", 24))
status_label.pack()


def play_unpleasant_sound():
    pygame.mixer.music.load("sound/siren.mp3")
    pygame.mixer.music.play(-1)


def stop_unpleasant_sound():
    pygame.mixer.music.stop()


"""  Function to update the video frame """
def update_video_frame():
    _, img = cap.read()
    if img is not None:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)

        """ Check if the video has been paused for more than 3 seconds """
        if film_status == "paused" and paused_time is not None:
            elapsed_time = time.time() - paused_time
            if elapsed_time > 3:
                """  Flashing exclamation marks on the video frame """
                if int(time.time() * 2) % 2 == 0:
                    cv2.putText(img, "!!!!!", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 6, (255, 0, 0), 11)
                    play_unpleasant_sound()

        img = Image.fromarray(img)
        video_frame.imgtk = ImageTk.PhotoImage(image=img)
        video_frame.configure(image=video_frame.imgtk)

    """ Set delay for 33 fps """
    root.after(33, update_video_frame)


""" Function to check face recognition and film status """
def check_face_recognition():
    global consecutive_closed_eyes, consecutive_open_eyes, film_status, paused_time

    ret, img = cap.read()
    if ret:
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        """ Detect faces in the image """
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        if len(faces) > 0:
            """ Rectangle around the faces """
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            """ Extract the region of interest for eyes detection """
            roi_gray = frame[y:y + h, x:x + w]
            eyes = eyeCascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
            )

            if len(eyes) == 0:
                print('No eyes!!!!')
                consecutive_closed_eyes += 1
                consecutive_open_eyes = 0

                """ 
                Check for consecutive closed eyes, 
                Simulate 'k' key to pause the video, 
                Record the time when video was paused,
                Reset counter
                """
                if consecutive_closed_eyes >= threshold_closed_eyes and film_status == "running":
                    pyautogui.press('k')
                    film_status = "paused"
                    paused_time = time.time()
                    consecutive_closed_eyes = 0

            else:
                print('Eyes!')
                consecutive_open_eyes += 1
                consecutive_closed_eyes = 0

                """  Check for consecutive open eyes """
                if consecutive_open_eyes >= threshold_open_eyes and film_status == "paused":
                    pyautogui.press('k')
                    film_status = "running"
                    consecutive_open_eyes = 0
                    stop_unpleasant_sound()

        """ Update the status label with the current film status and color """
        status_label.config(text=f"Status: {film_status}", fg="red" if film_status == "paused" else "green")

    """ Check every 100 ms """
    root.after(100, check_face_recognition)


"""  Start the Tkinter main loop """
root.after(0, update_video_frame)
root.after(0, check_face_recognition)
root.mainloop()