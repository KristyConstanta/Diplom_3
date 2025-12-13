from selenium.webdriver.common.by import By

# показать/скрыть пароль (глаз) в поле Пароль
SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']")

# поле ввода Пароль
RESET_PASSWORD_FIELD = (By.XPATH, "//div[@class='input__icon input__icon-action']/parent::div")