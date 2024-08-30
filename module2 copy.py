from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

# Инициализация браузера Chrome
browser = webdriver.Chrome()

# Открытие веб-страницы
browser.get("https://igroutka.ru/igry-klikery/46414-kliker-kapibar.html")

# Ожидание загрузки страницы
time.sleep(40)

print('poshel')
# Поиск элемента на сайте (измените путь к элементу при необходимости)
body = browser.find_element(By.ID, 'main-game')

# Инициализация ActionChains
actions = ActionChains(browser)

# Выполнение кликов по координатам внутри элемента
for i in range(0, 100):
    print(i)
    time.sleep(1)
    actions.move_to_element_with_offset(body, 340, 320).click().perform()

# Закрыть браузер после завершения
