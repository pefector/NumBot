from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Message staff
contact = "מתגברים על סביון"
text = "שלום מה קורה יא אח"

# Opening chrome
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

# Search for group
SearchBoxXPath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
SearchBox = driver.find_element_by_xpath(SearchBoxXPath)
SearchBox.click()
time.sleep(0.5)

SearchBox.send_keys(contact)
SearchBox.send_keys('\n')
time.sleep(0.5)

# Send message
TypeBoxXPath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
TypeBox = driver.find_element_by_xpath(TypeBoxXPath)
TypeBox.click()
time.sleep(0.3)

TypeBox.send_keys(text)
TypeBox.send_keys('\n')

test = '//*[@id="main"]/div[3]/div/div/div[3]/div[13]/div/div/div/div[2]/div/span/span'

# driver.quit()