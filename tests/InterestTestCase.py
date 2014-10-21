#coding=utf-8

__author__ = 'popka'

import unittest
import tests.Utils.Utils as utils
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait
from tests.Pages.CreatePage import CreatePage
import os

class InterestTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        InterestTest.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        utils.auth(driver=InterestTest.driver)


    @classmethod
    def tearDownClass(cls):
        InterestTest.driver.quit()

    def setUp(self):
        self.create_page = CreatePage(InterestTest.driver)
        self.create_page.open()

        utils.wait_for_create_page_load(InterestTest.driver)
        utils.wait_for_ajax_complete(InterestTest.driver)

        utils.fill_require(self.driver, self.create_page)
        utils.wait_for_ajax_complete(self.driver)

        self.interest = self.create_page.interest


    def test_check_business(self):

        self.interest.open_interest()
        self.interest.check_business()
        utils.wait_for_ajax_complete(self.driver)

        self.create_page.submit()
        utils.wait_for_ajax_complete(driver=self.driver)

        edit_page = utils.open_last_details(driver=self.driver)

        interest_form = edit_page.interest_form
        utils.wait_for_ajax_complete(driver=self.driver)
        self.assertTrue(interest_form.is_business_selected())


    def test_check_inside(self):
        array_name = ["Малый бизнес"]

        self.interest.open_interest()
        utils.wait_for_ajax_complete(self.driver)
        self.interest.open_business()

        self.interest.click_element(array_name[0])
        utils.wait_for_ajax_complete(self.driver)

        self.create_page.submit()
        utils.wait_for_ajax_complete(driver=self.driver)

        edit_page = utils.open_last_details(driver=self.driver)

        interest_form = edit_page.interest_form
        utils.wait_for_ajax_complete(driver=self.driver)
        self.assertTrue(interest_form.is_selected(array_name))


    def test_check_more_than_six(self):
        array_name = ["B2B", "Малый бизнес", "Управление персоналом",
                      "Финансы и бухгалтерский учет", "Юридическая поддержка",
                      "B2B / Для офиса", "B2B / Документальная и финансово-правовая поддержка"]

        self.interest.open_interest()
        utils.wait_for_ajax_complete(self.driver)
        self.interest.open_business()

        self.interest.click_element(array_name[0])
        self.interest.click_element(array_name[1])
        self.interest.click_element(array_name[2])
        self.interest.click_element(array_name[3])
        self.interest.click_element(array_name[4])
        self.interest.click_element(array_name[5])
        self.interest.click_element(array_name[6])
        utils.wait_for_ajax_complete(self.driver)

        self.create_page.submit()
        utils.wait_for_ajax_complete(driver=self.driver)

        edit_page = utils.open_last_details(driver=self.driver)

        interest_form = edit_page.interest_form
        utils.wait_for_ajax_complete(driver=self.driver)
        self.assertTrue(interest_form.is_selected(array_name))


    def test_cancel_element(self):
        array_name_short = ["B2B"]
        array_name_long = ["B2B", "Малый бизнес"]

        self.interest.open_interest()
        utils.wait_for_ajax_complete(self.driver)
        self.interest.open_business()

        self.interest.click_element(array_name_long[0])
        self.interest.click_element(array_name_long[1])
        self.interest.click_element(array_name_long[1])
        utils.wait_for_ajax_complete(self.driver)

        self.create_page.submit()
        utils.wait_for_ajax_complete(driver=self.driver)

        edit_page = utils.open_last_details(driver=self.driver)

        interest_form = edit_page.interest_form
        utils.wait_for_ajax_complete(driver=self.driver)
        self.assertTrue(interest_form.is_selected(array_name_short))


    def test_save_on_close(self):
        array_name = ["B2B"]

        self.interest.open_interest()
        utils.wait_for_ajax_complete(self.driver)

        self.interest.open_business()
        self.interest.click_element(array_name[0])
        self.interest.open_business()

        utils.wait_for_ajax_complete(self.driver)
        self.create_page.submit()
        utils.wait_for_ajax_complete(driver=self.driver)

        edit_page = utils.open_last_details(driver=self.driver)

        interest_form = edit_page.interest_form
        utils.wait_for_ajax_complete(driver=self.driver)
        self.assertTrue(interest_form.is_selected(array_name))