from page_objects.home_page import HomePageBurger
from page_objects.login_page import LoginPageBurger
from page_objects.account_page import AccountPageBurger
import allure
import locators.login_page_locators
import urls


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на "Личный кабинет"')
    @allure.description('При клике на кнопку "Личный кабинет" происходит переход на страницу авторизации')
    def test_lk_button_redirect(self, driver):
        home_page = HomePageBurger(driver)
        home_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        current_url = login_page.get_current_url()
        assert current_url == urls.BASE_URL + "/" + urls.LOGIN_ENDPOINT

    @allure.title('Проверка перехода в раздел "История заказов"')
    @allure.description('При клике на кнопку "История заказов" в личном кабинете происходит переход в раздел '
                        '"История заказов"')
    def test_redirect_to_orders_history(self, driver, default_user):
        home_page = HomePageBurger(driver)
        home_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.input_email(default_user['email'])
        login_page.input_password(default_user['password'])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.click_lk_button()
        account_page = AccountPageBurger(driver)
        account_page.click_orders_history_button()
        current_url = account_page.get_current_url()
        assert current_url == urls.BASE_URL + "/" + urls.ORDER_HISTORY_ENDPOINT

    @allure.title('Проверка выхода пользователя из аккаунта')
    @allure.description('При клике на кнопку "Выход" в личном кабинете происходит выход из аккаунта и переход на '
                        'страницу авторизации')
    def test_logout(self, driver, default_user):
        home_page = HomePageBurger(driver)
        home_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.input_email(default_user['email'])
        login_page.input_password(default_user['password'])
        login_page.click_login_submit_button()
        home_page.wait_home_page_loading()
        home_page.click_lk_button()
        account_page = AccountPageBurger(driver)
        account_page.click_logout_button()
        account_page.wait_redirect()
        current_url = login_page.get_current_url()
        assert current_url == urls.BASE_URL + "/" + urls.LOGIN_ENDPOINT