from selenium.webdriver.common.by import By

LK_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка Личный кабинет
ORDER_FEED_BUTTON = (By.XPATH,  "//p[text()='Лента Заказов']")  # кнопка Лента Заказов
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка Оформить заказ
TITLE = (By.XPATH, "//h1")  # главный заголовок главной страницы

INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")
INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")  # счетчик ингредиента
CONSTRUCTOR_BASKET = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")  # корзина-конструктор заказа

WINDOW_WITH_DETAILS_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']") # заголовок окна с деталями ингредиента
WINDOW_WITH_DETAILS_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]//button")

WINDOW_ORDER_TITLE = (By.XPATH, "//p[text()='идентификатор заказа']")  # заголовок в окне оформленного заказа
WINDOW_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")  # номер заказа
WINDOW_ORDER_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")