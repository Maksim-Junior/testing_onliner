from selenium import webdriver
import unittest

from onliner import HelperOnliner


class PlayGround(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_onliner(self):
        browser = self.driver
        page = HelperOnliner(browser)
        page.go_to_site()
        page.go_to_catalog()
        page.go_to_electronic()
        page.go_to_mobiles()
        page.click_to_phones()
        page.select_phone()
        price = page.find_price()
        phone_name = page.get_phone_name()
        page.search_area(phone_name)
        page.switch_to_iframe()
        iframe_price = page.price_iframe()
        self.assertEqual(price, iframe_price)

    def tearDown(self):
        self.driver.quit()
