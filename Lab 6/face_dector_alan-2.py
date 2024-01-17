import cv2
import pyautogui
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

# Load face and eye cascade classifiers
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

# Counter to track consecutive closed eyes
consecutive_closed_eyes = 0
consecutive_open_eyes = 0
threshold_closed_eyes = 3  # Adjust this threshold as needed
threshold_open_eyes = 7

# YouTube video URL
youtube_video_url = "https://www.youtube.com/watch?v=To7ZFqKDnng"  # Replace with your video ID

# Open the YouTube video in the default web browser
webbrowser.open(youtube_video_url, new=2)
# Film status flag
film_status = "running"

# Function to update the video frame
def update_video_frame():
    _, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)
    img = Image.fromarray(img)
    video_frame.imgtk = ImageTk.PhotoImage(image=img)
    video_frame.configure(image=video_frame.imgtk)
    video_frame.after(33, update_video_frame)  # Set delay for 30 fps

# Function to check face recognition and film status
def check_face_recognition():
    global consecutive_closed_eyes, consecutive_open_eyes, film_status

    ret, img = cap.read()
    if ret:
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        if len(faces) > 0:
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Extract the region of interest for eyes detection
            roi_gray = frame[y:y + h, x:x + w]
            eyes = eyeCascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
            )

            if len(eyes) == 0:
                print('No eyes!!!')
                consecutive_closed_eyes += 1
                consecutive_open_eyes = 0

                # Check for consecutive closed eyes
                if consecutive_closed_eyes >= threshold_closed_eyes and film_status == "running":
                    print('Pause the video, film status {}, eyes closed in row {}'.format(film_status,consecutive_closed_eyes))
                    pyautogui.press('k')  # Simulate 'k' key to pause the video
                    film_status = "paused"
                    consecutive_closed_eyes = 0  # Reset counter

            else:
                print('Eyes!!!')
                consecutive_open_eyes += 1
                consecutive_closed_eyes = 0

                # Check for consecutive open eyes
                if consecutive_open_eyes >= threshold_open_eyes and film_status == "paused":
                    print('Play the video, film status {}, eyes closed in row {}'.format(film_status,consecutive_open_eyes))
                    pyautogui.press('k')  # Simulate 'k' key to play the video
                    film_status = "running"
                    consecutive_open_eyes = 0  # Reset counter

        img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_LINEAR)
        img = Image.fromarray(img)
        video_frame.imgtk = ImageTk.PhotoImage(image=img)
        video_frame.configure(image=video_frame.imgtk)

    video_frame.after(33, check_face_recognition)  # Set delay for 30 fps

# Function to close the YouTube video window
def close_youtube_window():
    # Implement window closing logic here
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Face Recognition")

# Create frame for face recognition
video_frame = tk.Label(root)
video_frame.pack()

# Button to close the YouTube video window
close_button = tk.Button(root, text="Close YouTube Window", command=close_youtube_window)
close_button.pack()

# Call the functions to update frames
update_video_frame()
check_face_recognition()

# Start the Tkinter main loop
root.mainloop()
