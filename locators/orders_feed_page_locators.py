from selenium.webdriver.common.by import By

CONSTRUCT_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка Конструктор
LK_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка Личный кабинет

ORDER = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem__2x95r')][1]")  # последний заказ из Ленты заказов

# номер последнего заказа из Ленты заказов
ORDER_NUMBER_FROM_FEED = (
    By.XPATH, "//a[@class='OrderHistory_link__1iNby'][1]//p[contains(text(), 'Сегодня')]/preceding-sibling::p")

WINDOW_WITH_INFO = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]")  # всплывающее окно с деталями заказа

COUNTER_ALL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Выполнено за всё время
COUNTER_TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # Выполнено за сегодня

# поле с номером заказа из раздела В работе
ORDER_IN_WORK = (By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem li.text_type_digits-default")