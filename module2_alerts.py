from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/alert_accept.html")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()

    x = int(driver.find_element(By.ID, "input_value").text)
    driver.find_element(By.ID, "answer").send_keys(calc(x))
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(10)
    driver.quit()