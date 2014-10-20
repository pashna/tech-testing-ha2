__author__ = 'popka'
import unittest
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from tests.Utils.Utils import auth
from selenium.webdriver.support.ui import WebDriverWait
import tests.Utils.Utils as utils
from tests.Pages.CampaignsPage import CampaignsPage
import random

class ReloadPageTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = DesiredCapabilities.FIREFOX.copy()
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=self.browser
        )



    def tearDown(self):
        self.driver = self.driver.quit()

    def test_correct_fill_form(self):

        create_page = auth(self.driver)
        utils.fill_require(self.driver, create_page)

        title = create_page.get_title()
        create_page.submit()

        utils.wait_for_ajax_complete(driver=self.driver)

        campaigns_page = CampaignsPage(self.driver)
        campaigns_page.open()

        utils.wait_for_campaigns_page_load(driver=self.driver)
        utils.wait_for_ajax_complete(driver=self.driver)

        text = campaigns_page.central_part.get_page_source()

        self.assertTrue(text.index(title) > 0)


    def test_error_fill_form__no_header(self):

        create_page = auth(self.driver)
        utils.fill_require(driver=self.driver, create_page=create_page, HEADER='')

        utils.wait_for_ajax_complete(driver=self.driver)

        title = create_page.get_title()
        create_page.submit()

        utils.wait_for_ajax_complete(driver=self.driver)

        campaigns_page = CampaignsPage(self.driver)
        campaigns_page.open()

        utils.wait_for_ajax_complete(driver=self.driver)
        utils.wait_for_campaigns_page_load(driver=self.driver)

        text = campaigns_page.central_part.get_page_source()

        self.assertRaises(ValueError, text.index, title)

