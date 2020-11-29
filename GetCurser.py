import cv2
from PIL import ImageGrab
import numpy as np
from pynput.mouse import Listener

point1 = (0, 0)
point2 = (0, 0)

trys = 0


def on_click(x, y, button, pressed):
    global point1, point2, trys
    if pressed:
        if str(button) == "Button.left":
            point1 = (x, y)
        elif str(button) == "Button.right":
            point2 = (x, y)
        else:
            print(f"\n======{trys}======")
            print("x1, y1, x2, y2 : ", *point1, *point2)
            print(f"======{trys}======\n")
            trys += 1
            gmi = ImageGrab.grab(bbox=[*point1, *point2])
            gmip = np.array(gmi.getdata(), dtype='uint8').reshape((gmi.size[1], gmi.size[0], 3))
            cv2.imshow('window', gmip)
            cv2.waitKey()
        point1, point2 = (min(point1[0], point2[0]), min(point1[1], point2[1])), (
                          max(point1[0], point2[0]), max(point1[1], point2[1]))
        print(f'{button} at ({x}, {y})')


# on_move=on_move, on_click=on_click, on_scroll=on_scroll

with Listener(on_click=on_click) as listener:
    listener.join()