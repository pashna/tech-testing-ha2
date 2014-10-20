#coding=utf-8
import unittest
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from tests.Utils.Utils import auth
from selenium.webdriver.support.ui import WebDriverWait
from tests.Utils.Utils import ajax_complete

class AuthTestCase(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass
        #self.driver.quit()

    @classmethod
    def setUpClass(cls):
        AuthTestCase.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            #desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
        )

    @classmethod
    def tearDownClass(cls):
        AuthTestCase.driver.quit()

    def fillRequire(self):
        pass

    #Проверяем, прикрепится ли информация при передачи ссылки
    #ПОЧЕМУ-то не проходит! AJAX не выполняется! ГАВНО!
    def test_correct_fill_from_link(self):

        LINK = 'play.google.com/store/apps/details?id=org.bmstu.BmstuSchedule&hl=ru'
        HEADER = 'BMSTU DASHBOARD'
        TEXT = 'AMAZING APPLICATION! FOR YOU, FOR ME, FOR YOUR CAT'
        BIG_PHOTO = 'banner.jpg'
        SMALL_PHOTO = 'icon.jpg'


        create_page = auth(self.driver)

        create_page.set_radio_mobile_app()
        create_page.set_lenta()

        reqire_menu = create_page.require_menu
        reqire_menu.set_link(LINK)

        WebDriverWait(self.driver, 30, 10).until(ajax_complete, 'AJAX')
        reqire_menu.set_header(HEADER)
        reqire_menu.set_text(TEXT)
        reqire_menu.set_big_photo(BIG_PHOTO)
        reqire_menu.set_small_photo(SMALL_PHOTO)

















