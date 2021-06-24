from BaseApp import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Locators:
    LINK_CATALOG = (By.CLASS_NAME, "b-main-navigation__link")

    LINK_ELECTRONIC = (By.CLASS_NAME, "catalog-navigation-classifier__item ")

    PHONES_ELECTRONICS = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']//"
                                    "div[@class='g-middle-i']/div[1]/div[3]/div/div[1]/div[1]/div/div[1]/"
                                    "div[@class='catalog-navigation-list__aside-title']")

    PHONES = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']/"
                        "div[@class='l-gradient-wrapper']//div[@class='g-middle-i']/"
                        "div[1]/div[3]/div/div[1]/div[1]/div/div[1]/div[@class='catalog-navigation-list__dropdown']/"
                        "div[@class='catalog-navigation-list__dropdown-list']/a[@href='https://"
                        "catalog.onliner.by/mobile']//span[@class='catalog-navigation-list__dropdown-description']")

    PHONE = (By.XPATH, "/html//div[@id='schema-products']/div[7]/"
                       "div[@class='schema-product schema-product_narrow-sizes']/"
                       "div[@class='schema-product__part schema-product__part_2']/"
                       "div[@class='schema-product__part schema-product__part_4']/"
                       "div[@class='schema-product__title']/a[@href='https://"
                       "catalog.onliner.by/mobile/apple/iphone1164b']/span[.='Смартфон Apple iPhone 11 64GB (черный)']")

    PRICE = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']/"
                       "div[@class='l-gradient-wrapper']/div[@class='g-middle']/"
                       "div[@class='g-middle-i']/div[@class='catalog-content js-scrolling-area']/"
                       "div[1]//div[@class='offers-description__price offers-description__price_primary']/"
                       "a[@href='https://catalog.onliner.by/mobile/apple/iphone1164b/prices']")

    INPUT_AREA = (By.XPATH, "//div[@id='fast-search']/form[@action='//"
                            "catalog.onliner.by/search/']/input[@name='query']")

    PHONE_NAME = (By.XPATH, "/html//div[@id='container']/div[@class='g-container-outer']/"
                            "div[@class='l-gradient-wrapper']/div[@class='g-middle']//"
                            "h1[@class='catalog-masthead__title']")

    IFRAME = (By.CLASS_NAME, "modal-iframe")

    PRICE_IFRAME = (By.XPATH, "//div[@id='search-page']/div[@class='search__content-wrapper']/"
                              "ul[@class='search__results']/li[1]//div[@class='product__price']/a[1]/span")


class HelperOnliner(Base):
    def go_to_catalog(self):
        return self.find_element(Locators.LINK_CATALOG, time=2).click()

    def go_to_electronic(self):
        return self.find_element(Locators.LINK_ELECTRONIC, time=2).click()

    def go_to_mobiles(self):
        phones = self.find_element(Locators.PHONES_ELECTRONICS, time=2)
        move_to_element = ActionChains(self.driver).move_to_element(phones)
        return move_to_element.perform()

    def click_to_phones(self):
        return self.find_element(Locators.PHONES, time=2).click()

    def select_phone(self):
        return self.find_element(Locators.PHONE, time=2).click()

    def find_price(self):
        return self.find_element(Locators.PRICE, time=2).text

    def get_phone_name(self):
        return self.find_element(Locators.PHONE_NAME, time=2).text

    def search_area(self, search_text):
        return self.find_element(Locators.INPUT_AREA, time=2).send_keys(f'{search_text}')

    def switch_to_iframe(self):
        iframe = self.find_element(Locators.IFRAME, time=2)
        return self.driver.switch_to.frame(iframe)

    def price_iframe(self):
        return self.find_element(Locators.PRICE_IFRAME, time=2).text
