from selenium.webdriver.support.wait import WebDriverWait
from tests.Pages.Component import Component
from tests.Pages.Page import Page
from selenium.webdriver import ActionChains

__author__ = 'popka'


class CreatePage(Page):
    PATH = '/ads/create'
    MOBILE = '#product-type-6039'
    LENTA = '#pad-mobile_app_feed'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def slider(self):
        return Slider(self.driver)

    def setRadioMobileApp(self):
        self.driver.find_element_by_css_selector(self.MOBILE).click()

    def setLenta(self):
        self.driver.find_element_by_css_selector(self.LENTA).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class Slider(Component):
    SLIDER = '.price-slider__begunok'

    def move(self, offset):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SLIDER)
        )
        ac = ActionChains(self.driver)
        ac.click_and_hold(element).move_by_offset(offset, 0).perform()