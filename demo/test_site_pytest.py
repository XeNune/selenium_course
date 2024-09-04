import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_open_login_page(driver):
    link = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver.get(link)
    assert "OrangeHRM" in driver.title

def test_login_component_loaded(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "auth-login"))
    )
    assert driver.find_element(By.TAG_NAME, "auth-login") is not None

def test_find_login_button(driver):
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
    )
    assert login_button is not None

def test_login_with_credentials(driver):
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
    )
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    
    # Проверяем, что успешный вход был выполнен
    dashboard_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module"))
    ).text
    assert "Dashboard" in dashboard_text

def test_main_menu_loaded(driver):
    main_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.oxd-main-menu"))
    )
    assert main_menu is not None

def test_click_first_menu_item(driver):
    main_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.oxd-main-menu"))
    )
    first_menu_item = WebDriverWait(main_menu, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "li"))
    )
    first_menu_item.click()
    
    # Проверяем, что первый пункт меню был успешно нажат
    current_url = driver.current_url
    assert "viewSystemUsers" in current_url

def test_employee_count_matches(driver):
    number_of_employee = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-horizontal-padding.orangehrm-vertical-padding span.oxd-text--span"))
    ).text

    employee = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.orangehrm-container'))
    )
    employee_cards = employee.find_elements(By.CSS_SELECTOR, '.oxd-table-card')
    count = len(employee_cards)
    assert str(count) in number_of_employee

def test_click_fourth_menu_item(driver):
    time.sleep(2)
    fourth_menu_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(n+4)"))
    )
    fourth_menu_item.click()
    
    # Проверяем, что четвертый пункт меню был успешно нажат
    current_url = driver.current_url
    assert "viewEmployeeTimesheet" in current_url

def test_search_employee_name(driver):
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-table-body div[role='cell']:nth-child(3n+1) > div"))
    ).text
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]'))
    )
    input_element.send_keys(name)
    time.sleep(2)
    
    # Проверяем, что имя сотрудника было введено в поле поиска
    assert input_element.get_attribute('value') == name

def test_select_autocomplete_option(driver):
    time.sleep(2)
    innactive_elem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.oxd-autocomplete-dropdown.--positon-bottom"))
    )
    innactive_elem.click()
    
    # Проверяем, что опция автозаполнения была выбрана
    selected_option = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]').get_attribute('value')
    assert selected_option is not None

def test_submit_button_click(driver):
    time.sleep(2)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

def test_secondary_button_click(driver):
    time.sleep(4)
    secondary_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button"))
    )
    secondary_button.click()

def test_error_message_when_project_empty(driver):
    time.sleep(5)
    try:
        text_inside_input = driver.execute_script('return document.querySelector("input[placeholder=\'Type for hints...\']").value')
    except:
        text_inside_input = ''
    print(f"TEXT INSIDE INPUT: {text_inside_input}")
    time.sleep(5)
    if text_inside_input != '':
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        if save_button is None:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button--secondary"))
            )
        save_button.click()
        driver.find_element(By.CSS_SELECTOR, "button.oxd-button").click()
    else:
        time.sleep(5)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        button.click()

        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.oxd-text.oxd-text--span.oxd-input-group__message"))
        ).text

        assert error == "Select a Project", "No ERROR when project is empty."

        driver.find_element(By.CSS_SELECTOR, "button.oxd-button").click()
        time.sleep(5)

def test_status_update(driver):
    time.sleep(2)
    status_text = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.oxd-table-row div:nth-child(4n+1) div'), "Submitted")
    )
    if not status_text:
        driver.find_element(By.CSS_SELECTOR, "button.oxd-button--secondary").click()
        status_text = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.oxd-table-row div:nth-child(4n+1) div'), "Submitted")
        )
    # Проверяем, что статус был обновлен на "Submitted"
    assert status_text, "Error in edit Timesheet"

def test_user_name_update(driver):
    sixth_menu_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(n+6)"))
    )
    sixth_menu_item.click()
    time.sleep(5)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".orangehrm-horizontal-padding.orangehrm-vertical-padding"))
    )
    input_fields = driver.find_elements(By.CSS_SELECTOR, ".orangehrm-horizontal-padding.orangehrm-vertical-padding input")
    
    data = ["Ivanov", "Ivan", "Ivanovich"]

    for i in range(min(3, len(input_fields))):
        time.sleep(1)
        field = input_fields[i]
        while field.get_attribute("value") != "":
            field.send_keys(Keys.BACKSPACE)
            time.sleep(0.1)
        field.send_keys(data[i])
    
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    print("update info")
    driver.refresh()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-userdropdown-name")))
    assert data[0] in driver.find_element(By.CSS_SELECTOR, '.oxd-userdropdown-name').text, "Имя пользователя не изменилось."

def test_admin_menu(driver):
    ten_menu_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(n+10)"))
    )
    ten_menu_item.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
    driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee"

def test_employee_finding(driver):
    #Go to access records
    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(2n)")))
    button.click()
    #Find employee(me)
    input_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]'))
    )
    user_name = driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").text
    input_element.send_keys(user_name)

    time.sleep(5)
    bootom_elem = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='listbox']"))
    )
    bootom_elem.click()
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(5)
    assert driver.find_element(By.CLASS_NAME, "employee-image") is not None, "Employee not found"

