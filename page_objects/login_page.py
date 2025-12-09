import locators.login_page_locators
from page_objects.base_page import BasePageBurger
import urls
import allure


class LoginPageBurger(BasePageBurger):
    @allure.step('Ввод email в качестве логина пользователя на странице авторизации')
    def input_email(self, email):
        input_email = self.wait_and_find_element(locators.login_page_locators.LOGIN_EMAIL_FIELD)
        input_email.send_keys(email)

    @allure.step('Ввод пароля пользователя на странице авторизации')
    def input_password(self, password):
        input_password = self.wait_and_find_element(locators.login_page_locators.LOGIN_PASSWORD_FIELD)
        input_password.send_keys(password)

    @allure.step('Клик на кнопку "Войти" на странице авторизации')
    def click_login_submit_button(self):
        login_submit_button = self.wait_and_find_element(locators.login_page_locators.LOGIN_SUBMIT_BUTTON)
        login_submit_button.click()

    @allure.step('Клик на ссылку "Восстановить пароль" на странице авторизации')
    def click_recovery_password_link(self):
        recovery_password_link = self.wait_and_find_element(locators.login_page_locators.LINK_RECOVERY_PASSWORD)
        recovery_password_link.click()

    @allure.step('Проверка, что текущая страница это страница авторизации')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == urls.BASE_URL + urls.LOGIN_ENDPOINT