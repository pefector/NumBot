import time
from selenium import webdriver
import pytesseract as pt
import numpy as np
import cv2
from PIL import Image, ImageGrab
import keyboard


# pyTesseract setup
pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Selenium Setup
driver = webdriver.Chrome()
link = 'https://web.whatsapp.com/'
driver.get(link)

input("Press enter when logged in:")

# driver.execute_script("document.body.style.zoom=1")

# TestZoom
# while 1:
#     driver.execute_script(f"document.body.style.zoom="+input("num"))

# input box finding
TypeBoxXPath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
TypeBox = driver.find_element_by_xpath(TypeBoxXPath)

MinNumber = 0

time.sleep(0.3)


def Failed(where=""):
    global MinNumber, TypeBox, TypeBoxXPath
    num_in = input(f"Failed! ({where})\ninput current number : ")
    if num_in and num_in.isdigit():
        MinNumber = int(num_in)
    try:
        TypeBox = driver.find_element_by_xpath(TypeBoxXPath)
    except:
        Failed("You are fucked")
    return str(MinNumber)


# if doesnt sent message for x amount of time send next know num
WaitingCounter = 0

while 1:
    # Grabs numbers from screen
    try:
        gmi = ImageGrab.grab(bbox=(400, 900, 600, 930))
        text = pt.image_to_string(gmi)
        text = ''.join(list(filter(lambda n: n.isnumeric(), text)))
    except():
        text = Failed("Image capture failed")

    if keyboard.is_pressed('q') and keyboard.is_pressed('p'):
        text = Failed("Program stopped")

    if WaitingCounter == 70:
        text = str(MinNumber)

    if text:
        print("\n"+text)
        WaitingCounter = 0
        # Fail Switch
        num = int(text)
        if not MinNumber:
            MinNumber = num
        else:
            if (num - MinNumber > 30) or (MinNumber > num):
                num = MinNumber
            # elif MinNumber == num:
            #     continue

        try:
            # Send the current number
            TypeBox.click()
            TypeBox.send_keys(str(num+1))
            TypeBox.send_keys('\n')
            time.sleep(0.3)

            MinNumber = num + 1
        except:
            Failed("Textbox cant be found")
    else:
        print(end=".")
        WaitingCounter += 1