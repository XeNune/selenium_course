import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser_driver = webdriver.Chrome()
    yield browser_driver
    print("\nquit browser..")
    browser_driver.quit()

@pytest.fixture(autouse=True, scope="function")
def prepare_data():
    name = "Kira Yoshikage"
    return name


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        print()
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")