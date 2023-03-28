import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.sporcle.com/games/iurewhiuerw/numbers1_100")
element1=browser.find_element(By.XPATH,'//*[@id="button-play"]')
element1.click()
def input_to_element():
    element=browser.find_element(By.XPATH,'//*[@id="gameinput"]')
    input = 1
    while input < 101:
        element.send_keys(input)
        element.send_keys(" ")
        input = input+1
input_to_element()