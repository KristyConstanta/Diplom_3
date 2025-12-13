import locators.reset_password_page_lpcators
from page_objects.base_page import BasePageBurger
import urls
import allure


class ResetPasswordPageBurger(BasePageBurger):
    @allure.step('Клик на кнопку Показать/скрыть пароль в поле ввода пароля')
    def click_show_hide_button(self):
        submit_button = self.wait_and_find_element(locators.reset_password_page_lpcators.SHOW_HIDE_PASSWORD_BUTTON)
        submit_button.click()

    @allure.step('Проверка, что клик на кнопку Показать/скрыть пароль делает поле ввода пароля активным')
    def check_reset_password_field_is_active(self):
        reset_password_field = self.wait_and_find_element(locators.reset_password_page_lpcators.RESET_PASSWORD_FIELD)
        assert 'input_status_active' in reset_password_field.get_attribute('class')

    @allure.step('Проверка, что текущая сраница это страница установки нового пароля в процессе его восстановления')
    def check_current_url(self):
        current_url = self.get_current_url()
        assert current_url == urls.BASE_URL + urls.RESET_PASSWORD_ENDPOINT