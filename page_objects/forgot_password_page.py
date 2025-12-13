import locators.forgot_password_page_locators
from page_objects.base_page import BasePageBurger
import urls
import allure


class ForgotPasswordPageBurger(BasePageBurger):
    @allure.step('Ввод email на странице восстановления пароля')
    def input_email(self, email):
        input_email = self.wait_and_find_element(locators.forgot_password_page_locators.RECOVERY_EMAIL_FIELD)
        input_email.send_keys(email)

    @allure.step('Клик на кнопку "Восстановить" на странице восстановления пароля')
    def click_recovery_button(self):
        login_submit_button = self.wait_and_find_element(locators.forgot_password_page_locators.RECOVERY_BUTTON)
        login_submit_button.click()

    @allure.step('Проверка, что текущая страница это страница восстановления пароля')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == urls.BASE_URL + urls.FORGOT_PASSWORD_ENDPOINT

    @allure.step('Ожидание изменения url страницы"')
    def wait_redirect(self):
        return self.wait_url_change(urls.BASE_URL + urls.FORGOT_PASSWORD_ENDPOINT)