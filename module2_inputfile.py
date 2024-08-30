from selenium import webdriver
from selenium.webdriver.common.by import By

import os 
import time

try:
    driver = webdriver.Chrome()

    link = "https://suninjuly.github.io/file_input.html"
    driver.get(link)

    fields = driver.find_elements(By.CSS_SELECTOR, ".form-group input") 

    for field in fields:
        field.send_keys("KEK")
    workdir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(workdir, "file.txt")
    driver.find_element(By.CSS_SELECTOR, "form>input").send_keys(file_dir)
    driver.find_element(By.CSS_SELECTOR, "form button").click()
finally:
    time.sleep(10)
    driver.quit()