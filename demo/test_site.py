from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
link = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

driver.get(link)

try:
    # Wait for the login component to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "auth-login"))
    )
    print("Компонент логина загружен")
 
    # Wait for the login button to be present
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
    )
    print("Кнопка входа найдена")

    # Wait for the username and password fields to be present
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
    )
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    
    login_button.click()
    print("Успешный вход")
    
    # Wait for the main menu to be present
    main_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.oxd-main-menu"))
    )
    print("Список основного меню загружен")

    # Click the first menu item
    first_menu_item = WebDriverWait(main_menu, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "li"))
    )
    first_menu_item.click()
    print("Первый элемент меню успешно нажат.")

    # Wait for the employee number element to be present
    number_of_employee = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-horizontal-padding.orangehrm-vertical-padding span.oxd-text--span"))
    ).text

    count = 0
    flag = True

    while flag:
        employee = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.orangehrm-container'))
        )
        employee_cards = employee.find_elements(By.CSS_SELECTOR, '.oxd-table-card')
        count += len(employee_cards)

        try:
            next_page = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-pagination-page-item.oxd-pagination-page-item--previous-next .bi-chevron-right"))
            )
            next_page.click()
            time.sleep(2)
        except:
            flag = False
    assert str(count) in number_of_employee, "Неправильное отображение количества сотрудников"
    print("Количество сотрудников отображается верно")

    # Click on the 4th list item
    fourth_menu_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(n+4)"))
    )
    fourth_menu_item.click()

    # Get employee name and send to the input field
    name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-table-body div[role='cell']:nth-child(3n+1) > div"))
    ).text
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]'))
    )
    input_element.send_keys(name)

    time.sleep(5)
    # Wait for the autocomplete dropdown to appear and click on it
    innactive_elem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.oxd-autocomplete-dropdown.--positon-bottom"))
    )
    innactive_elem.click()

    # Click on the submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    # Click on the secondary button
    secondary_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button"))
    )
    secondary_button.click()


    # Check for the input field and handle it
    print("check for text in input")
    time.sleep(5)
    try:
        text_inside_input = driver.execute_script('return document.querySelector("input[placeholder=\'Type for hints...\']").value')
    except:
        text_inside_input = ''
    print(f"TEXT INSIDE INPUT: {text_inside_input}")
    time.sleep(5)
    if text_inside_input != '':
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        if button is None:
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button--secondary"))
            )
        button.click()
    else:
        print('Input field None')
        time.sleep(5)
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        if button is None:
            time.sleep(5)
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button--secondary"))
            )
            time.sleep(5)
        button.click()

        WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.oxd-text.oxd-text--span.oxd-input-group__message"))
        ).text
        assert error == "Select a Project", "No ERROR when project is empty."

        driver.find_element(By.CSS_SELECTOR, "button.oxd-button").click()
        time.sleep(5)
    
    # Wait for the status to be "Submitted"
    status_text = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.oxd-table-row div:nth-child(4n+1) div'), "Submitted")
    )
    assert status_text, "Error in edit time"



    sixth_menu_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(n+6)"))
    )
    sixth_menu_item.click()
    time.sleep(5)

    info = WebDriverWait(driver, 10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".orangehrm-horizontal-padding.orangehrm-vertical-padding"))
            )
    input_fields = driver.find_elements(By.CSS_SELECTOR, ".orangehrm-horizontal-padding.orangehrm-vertical-padding input")
    
    data = ["Alpatikov", "Aleksandr", "Aleksandrovich"]

    for i in range(min(3, len(input_fields))):
        time.sleep(1)
        field = input_fields[i]
        # Удаляем по одному символу
        while field.get_attribute("value") != "":
            field.send_keys(Keys.BACKSPACE)
            time.sleep(0.1)
        field.send_keys(data[i])
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    print("update info")
    driver.refresh()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-userdropdown-name")))
    assert data[0] in driver.find_element(By.CSS_SELECTOR, '.oxd-userdropdown-name').text, "Имя пользователя не изменилось."
    
    
except Exception as e:
    print("Произошла ошибка:", str(e))

finally:
    driver.quit()