#coding=utf-8

__author__ = 'popka'

import unittest
import tests.Utils.Utils as utils
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait
from tests.Pages.CreatePage import CreatePage

class InterestInterfaceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        InterestInterfaceTest.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            #desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
        )
        #utils.fill_require(InterestInterfaceTest.driver, create_page=InterestInterfaceTest.create_page)
        utils.auth(driver=InterestInterfaceTest.driver)


    @classmethod
    def tearDownClass(cls):
        InterestInterfaceTest.driver.quit()

    def setUp(self):
        self.create_page = CreatePage(InterestInterfaceTest.driver)
        self.create_page.open()
        utils.wait_for_create_page_load(InterestInterfaceTest.driver)
        utils.wait_for_ajax_complete(InterestInterfaceTest.driver)
        self.interest = self.create_page.interest


    def test_check_business(self):

        self.interest.open_interest()
        self.interest.check_business()
        utils.wait_for_ajax_complete(self.driver)
        self.assertTrue(self.interest.is_business_selected())


    def test_check_inside(self):
        array_name = ["Малый бизнес"]

        self.interest.open_interest()
        utils.wait_for_ajax_complete(self.driver)
        self.interest.open_business()

        self.interest.click_element(array_name[0])

        utils.wait_for_ajax_complete(self.driver)
        self.assertTrue(self.interest.is_selected(array_name))

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
        self.assertTrue(self.interest.is_selected(array_name))


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
        self.assertTrue(self.interest.is_selected(array_name_short))


    def test_save_on_close(self):
        array_name = ["B2B"]

        self.interest.open_interest()
        utils.wait_for_ajax_complete(self.driver)

        self.interest.open_business()
        self.interest.click_element(array_name[0])
        self.interest.open_business()

        utils.wait_for_ajax_complete(self.driver)
        self.assertTrue(self.interest.is_selected(array_name))

