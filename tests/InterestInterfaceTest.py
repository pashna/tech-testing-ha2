#coding=utf-8
__author__ = 'popka'

import unittest
import tests.Utils.Utils as utils
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

class InterestInterfaceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        InterestInterfaceTest.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            #desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
        )
        InterestInterfaceTest.create_page = utils.auth(driver=InterestInterfaceTest.driver)
        utils.fill_require(InterestInterfaceTest.driver, create_page=InterestInterfaceTest.create_page)


    @classmethod
    def tearDownClass(cls):
        InterestInterfaceTest.driver.quit()

    def setUp(self):
        self.interest = InterestInterfaceTest.create_page.interest


    def tearDown(self):
        self.interest.deselect_all()
        self.interest.hide_tree()

    def test_checked(self):
 #       array_name = ["Малый бизнес"]
#
#        self.interest.check_tumbler()
#        self.interest.click_element(array_name)
#        self.assertTrue(self.interest.is_checked(array_name))
        self.interest.open_interest()
        utils.wait_for_ajax_complete(self.driver)
        self.interest.open_business()
        self.interest.check_business()