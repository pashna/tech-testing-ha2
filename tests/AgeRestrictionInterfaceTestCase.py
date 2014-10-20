#coding=utf-8
import unittest
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from tests.Utils.Utils import auth
from selenium.webdriver.support.ui import WebDriverWait
from tests.Utils.Utils import ajax_complete
import tests.Utils.Utils as utils



class AgeRestrictionInterfaceTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        AgeRestrictionInterfaceTestCase.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            #desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
        )
        AgeRestrictionInterfaceTestCase.create_page = utils.auth(driver=AgeRestrictionInterfaceTestCase.driver)
        utils.fill_require(AgeRestrictionInterfaceTestCase.driver, create_page=AgeRestrictionInterfaceTestCase.create_page)


    @classmethod
    def tearDownClass(cls):
        AgeRestrictionInterfaceTestCase.driver.quit()



    def setUp(self):
        self.age_restriction = AgeRestrictionInterfaceTestCase.create_page.age_restriction

    def tearDown(self):
        self.age_restriction.close()


    #Работает ли выбор радио_баттона
    def test_age_restriction__select(self):
        VALUE = '6+'
        self.age_restriction.change_state()

        self.age_restriction.set_six()
        self.assertTrue(self.age_restriction.get_value() == VALUE)


    # Если ли возможность поменять выбор
    def test_age_restriction__change_choice(self):
        VALUE = '6+'
        self.age_restriction.change_state()

        self.age_restriction.set_six()
        self.age_restriction.set_zero()
        self.age_restriction.set_six()

        self.assertTrue(self.age_restriction.get_value() == VALUE)


    # Не потеряется ли выбор при закрытии панели
    def test_age_restriction__save_state_after_close(self):
        VALUE = '6+'
        self.age_restriction.change_state()

        self.age_restriction.set_six()
        self.age_restriction.change_state()

        self.assertTrue(self.age_restriction.get_value() == VALUE)