import unittest
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from tests.Utils.Utils import auth
from selenium.webdriver.support.ui import WebDriverWait

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

    def test(self):
        create_page = auth(self.driver)
        create_page.setRadioMobileApp()
        create_page.setLenta()
        #create_page.reqire_menu.set_link()
        elem = self.driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[1]/span[2]/input")

        elem.send_keys("www.yandex.ru")


        print(elem.get_attribute("value"))








