#coding=utf-8
import unittest
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from tests.Utils.Utils import auth
from selenium.webdriver.support.ui import WebDriverWait
from tests.Utils.Utils import ajax_complete
import tests.Utils.Utils as utils
from tests.Pages.CreatePage import CreatePage
import os



class AgeRestrictionTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''AgeRestrictionTestCase.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            #desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
        )
        '''
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        AgeRestrictionTestCase.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        utils.auth(driver=AgeRestrictionTestCase.driver)
        #utils.fill_require(AgeRestrictionInterfaceTestCase.driver, create_page=AgeRestrictionInterfaceTestCase.create_page)


    @classmethod
    def tearDownClass(cls):
        AgeRestrictionTestCase.driver.quit()



    def setUp(self):
        self.create_page = CreatePage(AgeRestrictionTestCase.driver)
        self.create_page.open()
        self.age_restriction = self.create_page.age_restriction

        utils.wait_for_create_page_load(AgeRestrictionTestCase.driver)
        utils.wait_for_ajax_complete(AgeRestrictionTestCase.driver)

        utils.fill_require(self.driver, self.create_page)
        utils.wait_for_ajax_complete(self.driver)


    #Работает ли выбор радио_баттона
    def test_age_restriction__select(self):
        VALUE = '6+'
        self.age_restriction.change_state()
        self.age_restriction.set_six()

        utils.wait_for_ajax_complete(self.driver)
        self.create_page.submit()

        utils.wait_for_ajax_complete(driver=self.driver)

        edit_page = utils.open_last_details(driver=self.driver)
        utils.wait_for_ajax_complete(driver=self.driver)
        self.assertTrue(edit_page.age_restriction_form.get_value() == VALUE)

    # Если ли возможность поменять выбор
    def test_age_restriction__change_choice(self):
        VALUE = '6+'
        self.age_restriction.change_state()

        self.age_restriction.set_six()
        self.age_restriction.set_zero()
        self.age_restriction.set_six()

        utils.wait_for_ajax_complete(self.driver)
        self.create_page.submit()

        utils.wait_for_ajax_complete(driver=self.driver)

        edit_page = utils.open_last_details(driver=self.driver)
        utils.wait_for_ajax_complete(driver=self.driver)
        self.assertTrue(edit_page.age_restriction_form.get_value() == VALUE)


    # Не потеряется ли выбор при закрытии панели
    def test_age_restriction__save_state_after_close(self):
        VALUE = '6+'
        self.age_restriction.change_state()

        self.age_restriction.set_six()
        self.age_restriction.change_state()

        utils.wait_for_ajax_complete(self.driver)
        self.create_page.submit()

        utils.wait_for_ajax_complete(driver=self.driver)

        edit_page = utils.open_last_details(driver=self.driver)
        utils.wait_for_ajax_complete(driver=self.driver)
        self.assertTrue(edit_page.age_restriction_form.get_value() == VALUE)