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
            #desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            desired_capabilities=self.browser
        )



    def tearDown(self):
        self.driver = self.driver.quit()

    def test_correct_fill_form(self):
        LINK = 'play.google.com/store/apps/details?id=org.bmstu.BmstuSchedule&hl=ru'
        HEADER = 'BMSTU DASHBOARD'
        TEXT = 'AMAZING APPLICATION! FOR YOU, FOR ME, FOR YOUR CAT'
        BIG_PHOTO = 'banner.jpg'
        SMALL_PHOTO = 'icon.jpg'

        title = utils.generate_random_word(5)


        create_page = auth(self.driver)

        create_page.set_title(title)
        title = create_page.get_title()
        create_page.set_radio_mobile_app()
        create_page.set_lenta()

        reqire_menu = create_page.reqire_menu
        reqire_menu.set_link(LINK)
        utils.wait_for_ajax_complete(driver=self.driver)

        reqire_menu.set_header(HEADER)
        reqire_menu.set_text(TEXT)
        reqire_menu.set_big_photo(BIG_PHOTO)
        reqire_menu.set_small_photo(SMALL_PHOTO)

        utils.wait_for_ajax_complete(driver=self.driver)

        create_page.submit()

        utils.wait_for_ajax_complete(driver=self.driver)

        campaigns_page = CampaignsPage(self.driver)
        campaigns_page.open()
        utils.wait_for_campaigns_page_load(driver=self.driver)
        utils.wait_for_ajax_complete(driver=self.driver)
        text = campaigns_page.get_page_source()

        self.assertTrue(text.index(title) > 0)



    def test_error_fill_form__no_header(self):
        LINK = 'play.google.com/store/apps/details?id=org.bmstu.BmstuSchedule&hl=ru'
        TEXT = 'AMAZING APPLICATION! FOR YOU, FOR ME, FOR YOUR CAT'
        BIG_PHOTO = 'banner.jpg'
        SMALL_PHOTO = 'icon.jpg'
        title = utils.generate_random_word(5)


        create_page = auth(self.driver)

        create_page.set_title(title)
        title = create_page.get_title()
        create_page.set_radio_mobile_app()
        create_page.set_lenta()

        reqire_menu = create_page.reqire_menu
        reqire_menu.set_link(LINK)
        utils.wait_for_ajax_complete(driver=self.driver)

        reqire_menu.set_text(TEXT)
        reqire_menu.set_big_photo(BIG_PHOTO)
        reqire_menu.set_small_photo(SMALL_PHOTO)

        utils.wait_for_ajax_complete(driver=self.driver)

        create_page.submit()

        utils.wait_for_ajax_complete(driver=self.driver)

        campaigns_page = CampaignsPage(self.driver)
        campaigns_page.open()

        utils.wait_for_ajax_complete(driver=self.driver)
        utils.wait_for_campaigns_page_load(driver=self.driver)
        
        text = campaigns_page.get_page_source()

        self.assertRaises(ValueError, text.index, title)