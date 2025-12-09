from page_objects.home_page import HomePageBurger
from page_objects.login_page import LoginPageBurger
from page_objects.orders_feed_page import OrderFeedPageBurger
from page_objects.account_page import AccountPageBurger
import allure


class TestOrdersFeed:

    @allure.title('Проверка появления вслывающего окна с деталями при клике на заказ')
    @allure.description('При клике на заказ в разделе "Лента заказов" появляется всплывающее окно с информацией по '
                        'этому заказу')
    def test_click_order_window_is_appear(self, driver):
        home_page = HomePageBurger(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrderFeedPageBurger(driver)
        order_feed_page.click_order_in_feed()
        order_feed_page.check_window_with_order_info_is_appear()

    @allure.title('Проверка, что заказы пользователя из "Истории заказов" отображаются на странице "Лента заказов"')
    @allure.description('Номер заказа пользователя, который отображается в разделе "История заказов" в личном '
                        'кабинете соответствует номеру заказа из раздела "Лента заказаов"')
    def test_user_orders_in_feed(self, driver, create_order):
        home_page = HomePageBurger(driver)
        home_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.input_email(create_order['user_email'])
        login_page.input_password(create_order['user_password'])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.click_lk_button()
        account_page = AccountPageBurger(driver)
        account_page.wait_account_page_loading()
        account_page.click_orders_history_button()
        order_number = account_page.get_order_number_from_history()
        order_feed_page = OrderFeedPageBurger(driver)
        order_feed_page.check_order_number_in_feed(order_number)

    @allure.title('Проверка,  что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Показатель счетчика "Выполнено за всё время" на странице Лента заказов до оформления заказа '
                        'пользователем будет меньше, показатель чем после оформления заказа')
    def test_create_new_order_counter_all_is_increased(self, driver, default_user):
        home_page = HomePageBurger(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrderFeedPageBurger(driver)
        order_count = order_feed_page.get_counter_all_orders()
        order_feed_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.input_email(default_user['email'])
        login_page.input_password(default_user['password'])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.move_ingredient_to_order()
        home_page.click_order_button()
        home_page.click_window_order_close_button()
        home_page.wait_home_page_loading()
        home_page.click_order_feed_button()
        order_feed_page.check_counter_all_orders_is_increased(order_count)

    @allure.title('Проверка,  что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Показатель счетчика "Выполнено за сегодня" на странице Лента заказов до оформления заказа '
                        'пользователем будет меньше, показатель чем после оформления заказа')
    def test_create_new_order_counter_today_is_increased(self, driver, default_user):
        home_page = HomePageBurger(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrderFeedPageBurger(driver)
        order_count = order_feed_page.get_counter_today_orders()
        order_feed_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.input_email(default_user['email'])
        login_page.input_password(default_user['password'])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.move_ingredient_to_order()
        home_page.click_order_button()
        home_page.click_window_order_close_button()
        home_page.wait_home_page_loading()
        home_page.click_order_feed_button()
        order_feed_page.check_counter_today_orders_is_increased(order_count)

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    @allure.description('Номер нового заказа пользователя отображается в разделе "В работе" на странице "Лента '
                        'заказаов"')
    def test_user_order_number_in_lst_order_in_work(self, driver, create_order):
        home_page = HomePageBurger(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrderFeedPageBurger(driver)
        order_number = create_order['order_number']
        order_feed_page.check_order_number_in_order_in_work(order_number)