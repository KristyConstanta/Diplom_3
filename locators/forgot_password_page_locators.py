from selenium.webdriver.common.by import By

RECOVERY_EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # поле ввода Email
RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # кнопка "Восстановить"