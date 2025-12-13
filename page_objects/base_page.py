from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePageBurger:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_loading(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def wait_element_invisible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    def wait_and_find_element(self, locator):
        self.wait_element_loading(locator)
        return self.driver.find_element(*locator)

    def click_element(self, element):
        return self.driver.execute_script("arguments[0].click();", element)

    def drag_and_drop_element(self, source_element, target_element):
        return drag_and_drop(self.driver, source_element, target_element)

    def wait_url_change(self, old_url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(old_url))

    def get_current_url(self):
        return self.driver.current_url