from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    driver.find_element(By.ID, "book").click()

    x = int(driver.find_element(By.ID, "input_value").text)
    driver.find_element(By.ID, "answer").send_keys(calc(x))
    driver.find_element(By.ID, "solve").click()
finally:
    time.sleep(10)
    driver.quit()