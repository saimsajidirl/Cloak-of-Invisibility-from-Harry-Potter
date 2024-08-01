# The Cloak of Invisibility was a magical artefact used to render the wearer invisible,
# and one of the fabled Deathly Hallows. In The Tale of the Three Brothers, it was the third
# and final Hallow created, supposedly by Death himself (who had the cloak in his possession
# at that time). Death bestowed this cloak to Ignotus Peverell after he requested something w
# ith the power to hide him if he were to go place to place without being followed by Death.


import cv2
import numpy as np
import time
import tkinter as tk
from tkinter import ttk

import sv_ttk
def color_selection():
    root = tk.Tk()
    root.title("Color Selection")
    root.geometry("1200x500")

    # Add welcome message
    welcome_label = tk.Label(root, text="Hi! I'm Muhammad Saim Sajid, the creator of this cloak. It's inspired by one of the Deathly Hallows, as the Greatest Wizard in history. This cloak is a gift from me to you.  Would you like to choose the color?")
    welcome_label.pack()

    def start_video():
        global color
        color = clicked.get()
        root.destroy()

    sv_ttk.set_theme("dark")

    clicked = tk.StringVar()
    clicked.set("red")
    radio_button1 = ttk.Radiobutton(root, text="Red", variable=clicked, value="red")
    radio_button2 = ttk.Radiobutton(root, text="Blue", variable=clicked, value="blue")

    radio_button1.pack()
    radio_button2.pack()

    start_button = ttk.Button(root, text="Start", command=start_video)
    start_button.pack()

    root.mainloop()

color_selection()

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(3)
for i in range(60):
    check, background = video.read()
background = np.flip(background, axis=1)

while(video.isOpened()):
    check, img = video.read()
    if check == False:
        break
    img = np.flip(img, axis=1)

    if color == "red":
        lower_color = np.array([0, 50, 50])
        upper_color = np.array([10, 255, 255])
    elif color == "blue":
        lower_color = np.array([100, 50, 50])
        upper_color = np.array([140, 255, 255])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    mask2 = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(img, img, mask=mask2)
    res2 = cv2.bitwise_and(background, background, mask=mask)
    final = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow("final", final)
    key = cv2.waitKey(1)
    if key == ord('c'):
        break

video.release()
cv2.destroyAllWindows()