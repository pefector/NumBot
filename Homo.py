import time
from selenium import webdriver
import pytesseract as pt
import numpy as np
import cv2
from PIL import Image, ImageGrab
import keyboard

# Selenium Setup
driver = webdriver.Chrome()
link = 'https://web.whatsapp.com/'
driver.get(link)

in_put = input("Press enter when logged in:")

# input box finding
TypeBoxXPath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
TypeBox = driver.find_element_by_xpath(TypeBoxXPath)

time.sleep(0.3)


def Failed(where=""):
    global TypeBox, TypeBoxXPath
    f = print if "Textbox" in where else input
    f(f"Failed! ({where})\ninput current number : ")
    TypeBox = driver.find_element_by_xpath(TypeBoxXPath)


i = int(in_put) if in_put else 0
while not keyboard.is_pressed('q'):
    pass
while 1:
    if keyboard.is_pressed('q') and keyboard.is_pressed('p'):
        Failed("Program stopped")

    try:
        # Send the current number
        TypeBox.click()
        TypeBox.send_keys(f"homo^{i}")
        TypeBox.send_keys('\n')
        time.sleep(0.18)

        i += 1
    except:
        Failed("Textbox cant be found")

    # input()
