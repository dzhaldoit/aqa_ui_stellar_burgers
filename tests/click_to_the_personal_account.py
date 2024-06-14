from selenium.webdriver.common.by import By
from selenium import webdriver


#Создание драйвера
driver = webdriver.Chrome()

#Открыть браузер и перейти на страницу
driver.get("https://stellarburgers.nomoreparties.site/")

#Нажать на кнопку "Войти в аккаунт"
driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

#Вводим логин и пароль
driver.find_element(By.NAME, "name").send_keys('dzha@mail.com')
driver.find_element(By.NAME, "Пароль").send_keys('12345qwerty')


#Нажать на кнопку "Войти"
driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

#Нажать на кнопку "Личный кабинет"
driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

#Проверка на переход
assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

driver.quit()