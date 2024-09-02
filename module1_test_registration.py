from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    field1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    field2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    field3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    
    field1.send_keys("ladno")
    field2.send_keys("ladno")
    field3.send_keys("ladno")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click() 
    time.sleep(1)
 
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1") 
    welcome_text = welcome_text_elt.text
 
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("done")

finally: 
    time.sleep(10) 
    browser.quit()