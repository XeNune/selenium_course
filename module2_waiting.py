from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    driver = webdriver.Chrome()
    # driver.implicitly_wait(10)

    # driver.get("https://suninjuly.github.io/wait1.html")
    # driver.find_element(By.ID, "verify").click()
    # message = driver.find_element(By.ID, "verify_message").text
    # print(message)
    # assert "successful" in message

    driver.get("https://suninjuly.github.io/wait2.html")
    innactive_elem = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    innactive_elem.click()

    message = driver.find_element(By.ID, "verify_message").text
    print(message)
    assert "successful" in message

finally:
    time.sleep(5)
    driver.quit()