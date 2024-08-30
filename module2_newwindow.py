from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/redirect_accept.html")
    driver.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    x = int(driver.find_element(By.ID, "input_value").text)
    driver.find_element(By.ID, "answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    
finally:
    time.sleep(10)
    driver.quit()