__author__ = 'popka'

import unittest
import tests.Utils.Utils as utils
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote

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