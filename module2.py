from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    #Open web
    browser.get("https://suninjuly.github.io/math.html")

    #Find element on site
    x_element = browser.find_element(By.ID, 'input_value')

    #Parcing text and calculate via function
    text_x_element = x_element.text
    answer = calc(text_x_element)

    #Find answer field and send keys
    browser.find_element(By.ID, 'answer').send_keys(answer)
    time.sleep(2)
    #Checkbox
    browser.find_element(By.ID, 'robotCheckbox').click()
    time.sleep(2)
    #Radiobutton
    browser.find_element(By.ID, 'robotsRule').click()
    time.sleep(2)
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()
