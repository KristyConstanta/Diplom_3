from page_objects.home_page import HomePageBurger
from page_objects.login_page import LoginPageBurger
from page_objects.forgot_password_page import ForgotPasswordPageBurger
from page_objects.reset_password_page import ResetPasswordPageBurger
import locators.forgot_password_page_locators
import locators.reset_password_page_lpcators
import urls
import allure


class TestPasswordRecovery:

    @allure.title('Проверка перехода по ссылке "Восстановить пароль"')
    @allure.description('При клике на ссылку "Восстановить пароль" на странице авторизации происходит переход на '
                        'страницу восстановление пароля')
    def test_recovery_password_link_redirect(self, driver):
        home_page = HomePageBurger(driver)
        home_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.click_recovery_password_link()
        forgot_password_page = ForgotPasswordPageBurger(driver)
        current_url = forgot_password_page.get_current_url()
        assert current_url == urls.BASE_URL + "/" + urls.FORGOT_PASSWORD_ENDPOINT

    @allure.title('Проверка ввода email и клика по кнопке "Восстановить"')
    @allure.description('После ввода email и клика на кнопку "Восстановить", происходит переход на страницу, '
                        'где можно установить новый пароль ')
    def test_input_email_and_click_recovery_button(self, driver, default_user):
        home_page = HomePageBurger(driver)
        home_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.click_recovery_password_link()
        forgot_password_page = ForgotPasswordPageBurger(driver)
        forgot_password_page.input_email(default_user['email'])
        forgot_password_page.click_recovery_button()
        forgot_password_page.wait_redirect()
        reset_password_page = ResetPasswordPageBurger(driver)
        current_url = reset_password_page.get_current_url()
        assert current_url == urls.BASE_URL + "/" + urls.RESET_PASSWORD_ENDPOINT

    @allure.title('Проверка клика на кнопку "Показать/скрыть пароль"')
    @allure.description('При клике на кнопку "Показать/скрыть пароль" поле Пароль становится активным')
    def test_click_show_hide_button_is_activated_field(self, driver, default_user):
        home_page = HomePageBurger(driver)
        home_page.click_lk_button()
        login_page = LoginPageBurger(driver)
        login_page.click_recovery_password_link()
        forgot_password_page = ForgotPasswordPageBurger(driver)
        forgot_password_page.input_email(default_user['email'])
        forgot_password_page.click_recovery_button()
        forgot_password_page.wait_redirect()
        reset_password_page = ResetPasswordPageBurger(driver)
        reset_password_page.click_show_hide_button()
        reset_password_field = reset_password_page.wait_and_find_element(locators.reset_password_page_lpcators.RESET_PASSWORD_FIELD)
        assert 'input_status_active' in reset_password_field.get_attribute('class')