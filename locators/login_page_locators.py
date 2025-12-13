from selenium.webdriver.common.by import By

LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # поле ввода Email
LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")  # поле ввода Пароль
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//Button[text()='Войти']")  # кнопка Войти
LINK_RECOVERY_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # ссылка Восстановить пароль