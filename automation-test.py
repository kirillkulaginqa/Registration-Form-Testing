# automation-test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("https://example.com/registration")  # URL формы регистрации

# Ввод данных в поля формы
driver.find_element(By.ID, "name").send_keys("Иван")
driver.find_element(By.ID, "email").send_keys("example@example.com")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "confirm_password").send_keys("password123")

# Нажатие на кнопку регистрации
driver.find_element(By.ID, "register").click()
time.sleep(2)

# Проверка успешной регистрации
success_message = driver.find_element(By.CLASS_NAME, "success").text
assert "Регистрация успешна" in success_message

driver.quit()
