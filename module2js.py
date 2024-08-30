from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    driver.get(link)
    x = driver.find_element(By.ID, "input_value").text
    answer = calc(x)
    driver.find_element(By.ID, "answer").send_keys(answer)

    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.ID, "robotsRule").click()

    button.click()
finally:
    time.sleep(10)
    driver.quit()