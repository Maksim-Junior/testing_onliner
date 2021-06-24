from selenium import webdriver
import unittest
import allure

from onliner import HelperOnliner


class PlayGround(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.feature('Testing Onliner')
    @allure.story('Prises equals test')
    def test_onliner(self):
        browser = self.driver
        page = HelperOnliner(browser)
        with allure.step('Go to the main page'):
            page.go_to_site()
        with allure.step('Go to the catalog'):
            page.go_to_catalog()
        with allure.step('Select category'):
            page.go_to_electronic()
        with allure.step('Select subcategory'):
            page.go_to_mobiles()
        with allure.step('Select mobiles'):
            page.click_to_phones()
        with allure.step('Click on the phone'):
            page.select_phone()
        with allure.step("Searching phone price"):
            price = page.find_price()
        with allure.step('Get phone name'):
            phone_name = page.get_phone_name()
        with allure.step('Searching phone by name'):
            page.search_area(phone_name)
        with allure.step('Switch to iframe'):
            page.switch_to_iframe()
        with allure.step('Searching phone price'):
            iframe_price = page.price_iframe()
        self.assertEqual(price, iframe_price)

    def tearDown(self):
        self.driver.quit()
