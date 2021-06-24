from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.onliner.by/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, resource=''):
        return self.driver.get(f'{self.base_url}{resource}')

    def switch_to_alert_accept(self):
        alert = Alert(self.driver)
        return alert.accept()