import locators.orders_feed_page_locators
from page_objects.base_page import BasePageBurger
import urls
import allure


class OrderFeedPageBurger(BasePageBurger):
    @allure.step('Клик на кнопку "Конструктор" в левом верхнем углу страницы Лента заказов')
    def click_construct_button(self):
        construct_button = self.wait_and_find_element(locators.orders_feed_page_locators.CONSTRUCT_BUTTON)
        construct_button.click()

    @allure.step('Клик на кнопку "Личный кабинет" в правом верхнем углу страницы Лента заказов')
    def click_lk_button(self):
        construct_button = self.wait_and_find_element(locators.orders_feed_page_locators.LK_BUTTON)
        construct_button.click()

    @allure.step('Клик на последний заказ в разделе Лента заказов')
    def click_order_in_feed(self):
        order = self.wait_and_find_element(locators.orders_feed_page_locators.ORDER)
        order.click()

    @allure.step('Получение номера последнео заказа в разделе Лента заказов')
    def get_last_order_number_from_feed(self):
        order_num = self.wait_and_find_element(locators.orders_feed_page_locators.ORDER_NUMBER_FROM_FEED)
        return int(order_num.text[2:])

    @allure.step('Получение значения счетчика "Выполнено за всё время"')
    def get_counter_all_orders(self):
        counter = self.wait_and_find_element(locators.orders_feed_page_locators.COUNTER_ALL_ORDERS)
        return int(counter.text)

    @allure.step('Получение значения счетчика "Выполнено за сегодня"')
    def get_counter_today_orders(self):
        counter = self.wait_and_find_element(locators.orders_feed_page_locators.COUNTER_TODAY_ORDERS)
        return int(counter.text)

    @allure.step('Получение номера заказа из раздела В работе')
    def get_number_of_order_in_work(self):
        order_num = self.wait_and_find_element(locators.orders_feed_page_locators.ORDER_IN_WORK)
        return int(order_num.text[1:])

    @allure.step('Проверка, что текущая страница это страница Ленты заказов')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == urls.BASE_URL + urls.FEED_ENDPOINT

    @allure.step('Проверка, что всплывающее окно с деталями заказа появляется')
    def check_window_with_order_info_is_appear(self):
        window = self.wait_and_find_element(locators.orders_feed_page_locators.WINDOW_WITH_INFO)
        assert window.is_displayed()

    @allure.step('Проверка, что номер заказа из раздела "История заказов" отображается в разделе Лента заказов')
    def check_order_number_in_feed(self, order_number_from_history):
        assert self.get_last_order_number_from_feed() == order_number_from_history

    @allure.step('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def check_counter_all_orders_is_increased(self, order_count):
        new_order_count = self.get_counter_all_orders()
        assert new_order_count > order_count

    @allure.step('Проверка, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def check_counter_today_orders_is_increased(self, order_count):
        new_order_count = self.get_counter_today_orders()
        assert new_order_count > order_count

    @allure.step('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    def check_order_number_in_order_in_work(self, order_number):
        assert self.get_number_of_order_in_work() == order_number