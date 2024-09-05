from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
link = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

driver.get(link)

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


############
############
############
# Click on the secondary button
edit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button"))
)
edit_button.click()
time.sleep(5)

try:
    text_inside_input = driver.execute_script('return document.querySelector("input[placeholder=\'Type for hints...\']").value')
except:
    text_inside_input = ''
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
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button.oxd-button").click()
    try:
        button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button--secondary"))
            )
        button.click()
    except:
        # driver.find_element(By.CSS_SELECTOR, "button.oxd-button").click()
        # time.sleep(5)
        pass

# Wait for the status to be "Submitted"
status_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.oxd-table-row div:nth-child(4n+1) div'), "Submitted")
)
assert status_text, "Error in edit time"


# ten_menu_item = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-child(n+10)"))
# )
# ten_menu_item.click()

# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
# driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("admin123")
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# #Go to access records
# button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(2n)")))
# button.click()
# #Find employee(me)
# input_element = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Type for hints..."]'))
# )
# user_name = driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").text
# input_element.send_keys(user_name)

# time.sleep(5)
# bootom_elem = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='listbox']"))
# )
# bootom_elem.click()
# driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
# time.sleep(5)
# assert driver.find_element(By.CLASS_NAME, "employee-image") is not None, "Картинки нет"
############
############
############
