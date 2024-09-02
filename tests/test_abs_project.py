import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistartionPage(unittest.TestCase):
    def test_page1(self):
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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
    
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()