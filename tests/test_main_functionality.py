from page_objects.home_page import HomePageBurger
from page_objects.login_page import LoginPageBurger
from page_objects.orders_feed_page import OrderFeedPageBurger
import allure


class TestMainFunctionality:

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    @allure.description('При клике на кнопку "Лента заказов" происходит переход на  страницу Лента заказов')
    def test_order_feed_button_redirect(self, driver):
        home_page = HomePageBurger(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrderFeedPageBurger(driver)
        order_feed_page.check_current_url()

    @allure.title('Проверка перехода по клику на "Конструктор"')
    @allure.description('При клике на кнопку "Конструктор" происходит переход на главную страницу')
    def test_construct_button_redirect(self, driver):
        home_page = HomePageBurger(driver)
        home_page.click_order_feed_button()
        order_feed_page = OrderFeedPageBurger(driver)
        order_feed_page.click_construct_button()
        home_page.check_current_url()

    @allure.title('Проверка появления вслывающего окна с деталями при клике на ингредиент')
    @allure.description('При клике на ингредиент появляется вслывающее окно с информацией об ингредиенте')
    def test_click_ingredient_window_is_appear(self, driver):
        home_page = HomePageBurger(driver)
        home_page.click_ingredient()
        home_page.check_window_with_ingredient_detail_is_appear()

    @allure.title('Проверка закрытия вслывающего окна с деталями при клике по крестику ')
    @allure.description('При клике на иконку с крестиком в правом вехнем углу окна окно закрывается')
    def test_close_window_with_detail(self, driver):
        home_page = HomePageBurger(driver)
        home_page.click_ingredient()
        home_page.click_window_with_detail_close_button()
        home_page.check_window_with_ingredient_detail_is_disappear()

    @allure.title('Проверка увеличения показателя счетчика ингредиента после добавлении ингредиента в заказ')
    @allure.description('После перемещения ингредента в корзину-конструктор значение его счетчика увеличивыется')
    def test_add_ingredient_in_order_counter_is_increased(self, driver):
        home_page = HomePageBurger(driver)
        home_page.move_ingredient_to_order()
        home_page.check_ingredient_counter_is_increased()

    @allure.title('Проверка успешности оформления заказа авторизованным пользователем')
    @allure.description('Авторизованный пользователсь оформляет заказ, после чего появляется всплывающее окно '
                        'с информацией о заказе')
    def test_create_order_success(self, driver, default_user):
        home_page = HomePageBurger(driver)
        home_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.input_email(default_user['email'])
        login_page.input_password(default_user['password'])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.move_ingredient_to_order()
        home_page.click_order_button()
        home_page.check_order_window_is_appear()