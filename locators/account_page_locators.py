from selenium.webdriver.common.by import By

ORDERS_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")  # кнопка История заказов
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка Выход
PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")  # кнопка Профиль

# номер заказа пользователя из раздела История заказов
ORDER_NUMBER_FROM_HISTORY = (
    By.XPATH, "//a[@class='OrderHistory_link__1iNby']//p[contains(text(), 'Сегодня')]/preceding-sibling::p")