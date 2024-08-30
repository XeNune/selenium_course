from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import math
import time

browser = webdriver.Chrome()

try:
    #Open web
    browser.get("https://suninjuly.github.io/selects2.html")

    #Find element on site
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    sum = num1 + num2

    print(num1)
    print(num2)
    print(sum)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum))

    browser.find_element(By.TAG_NAME, "button").click()
    
finally:
    time.sleep(10)
    browser.quit()
