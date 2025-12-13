import locators.account_page_locators
from page_objects.base_page import BasePageBurger
import urls
import allure


class AccountPageBurger(BasePageBurger):

    @allure.step('Ожидание полной загрузки страницы личного кабинета')
    def wait_account_page_loading(self):
        self.wait_element_loading(locators.account_page_locators.PROFILE_BUTTON)

    @allure.step('Клик на кнопку "История заказов" в личном кабинете')
    def click_orders_history_button(self):
        orders_history_link = self.wait_and_find_element(locators.account_page_locators.ORDERS_HISTORY_LINK)
        orders_history_link.click()

    @allure.step('Клик на кнопку "Выход" в личном кабинете')
    def click_logout_button(self):
        logout_button = self.wait_and_find_element(locators.account_page_locators.LOGOUT_BUTTON)
        logout_button.click()

    @allure.step('Получение номера заказа пользователя из раздела "История заказов"')
    def get_order_number_from_history(self):
        order_num = self.wait_and_find_element(locators.account_page_locators.ORDER_NUMBER_FROM_HISTORY)
        return int(order_num.text[2:])

    @allure.step('Ожидание изменения url страницы"')
    def wait_redirect(self):
        return self.wait_url_change(urls.BASE_URL + urls.ACCOUNT_ENDPOINT)

    @allure.step('Проверка, что текущая страница это страница История заказов в личном кабинете пользователя')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == urls.BASE_URL + urls.ORDER_HISTORY_ENDPOINT