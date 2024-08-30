from selenium import webdriver
from selenium.webdriver.common.by import By

import math
import time

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    #Open web
    browser.get("https://suninjuly.github.io/get_attribute.html")

    #Find element on site
    chest = browser.find_element(By.ID, 'treasure')
    x = chest.get_attribute("valuex")
    print(x)
    #Parcing text and calculate via function 
    answer = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(answer)
 
    #Checkbox
    browser.find_element(By.ID, 'robotCheckbox').click() 
    #Radiobutton
    browser.find_element(By.ID, 'robotsRule').click() 
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()
