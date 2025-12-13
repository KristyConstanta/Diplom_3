import locators.home_page_locators
from page_objects.base_page import BasePageBurger
import urls
import allure


class HomePageBurger(BasePageBurger):
    @allure.step('Ожидание полной загрузки главной страницы')
    def wait_home_page_loading(self):
        self.wait_element_loading(locators.home_page_locators.TITLE)

    @allure.step('Клик на кнопку Личный кабинет в правом верхнем углу главной страницы')
    def click_lk_button(self):
        lk_button = self.wait_and_find_element(locators.home_page_locators.LK_BUTTON)
        self.click_element(lk_button)

    @allure.step('Клик на кнопку Лента Заказов вверху главной страницы')
    def click_order_feed_button(self):
        order_feed_button = self.wait_and_find_element(locators.home_page_locators.ORDER_FEED_BUTTON)
        self.click_element(order_feed_button)

    @allure.step('Клик на ингредиент в разделе Конструктор на главной странице')
    def click_ingredient(self):
        ingredient = self.wait_and_find_element(locators.home_page_locators.INGREDIENT)
        self.click_element(ingredient)

    @allure.step('Клик на кнопку закрытия всплывающего окна с деталями ингредиента')
    def click_window_with_detail_close_button(self):
        close_button = self.wait_and_find_element(locators.home_page_locators.WINDOW_WITH_DETAILS_CLOSE_BUTTON)
        close_button.click()

    @allure.step('Клик на кнопку Оформить заказ')
    def click_order_button(self):
        order_button = self.wait_and_find_element(locators.home_page_locators.ORDER_BUTTON)
        self.click_element(order_button)

    @allure.step('Клик на кнопку закрытия окна оформленного заказа')
    def click_window_order_close_button(self):
        close_button = self.wait_and_find_element(locators.home_page_locators.WINDOW_ORDER_CLOSE_BUTTON)
        self.click_element(close_button)

    @allure.step('Перемещение ингредиента в корзину-конструктор')
    def move_ingredient_to_order(self):
        source_element = self.wait_and_find_element(locators.home_page_locators.INGREDIENT)
        target_element = self.wait_and_find_element(locators.home_page_locators.CONSTRUCTOR_BASKET)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Проверка, что текущая страница это главная страница')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == urls.BASE_URL

    @allure.step('Проверка, что всплывающее окно с деталями ингредиента появляется')
    def check_window_with_ingredient_detail_is_appear(self):
        title = self.wait_and_find_element(locators.home_page_locators.WINDOW_WITH_DETAILS_TITLE)
        assert title.is_displayed()

    @allure.step('Проверка, что всплывающее окно с деталями ингредиента закрывается')
    def check_window_with_ingredient_detail_is_disappear(self):
        title = self.wait_element_invisible(locators.home_page_locators.WINDOW_WITH_DETAILS_TITLE)
        assert not title.is_displayed()

    @allure.step('Проверка, что окно с информацией об успешном оформлении заказа появляется')
    def check_order_window_is_appear(self):
        title = self.wait_and_find_element(locators.home_page_locators.WINDOW_ORDER_TITLE)
        num = self.wait_and_find_element(locators.home_page_locators.WINDOW_ORDER_NUMBER)
        assert title.is_displayed() and num.text is not None

    @allure.step('Проверка увеличения показателя счетчика ингредиента после добавления его в корзину-конструктор')
    def check_ingredient_counter_is_increased(self):
        counter = self.wait_and_find_element(locators.home_page_locators.INGREDIENT_COUNTER)
        assert int(counter.text) > 0