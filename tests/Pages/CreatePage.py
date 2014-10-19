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
    def reqire_menu(self):
        return RequireMenu

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

class RequireMenu(Component):
    LINK = ".banner-form__input"

    LINK_VALUE = 'https://play.google.com/store/apps/details?id=org.bmstu.BmstuSchedule&hl=ru'
    SMALL_PICTURE_PATH = '/resourses/icon.jpg' #png doesnt work
    BIG_PICTURE_PATH = '/resourses/banner.jpg' #png doesnt work

    def set_link(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.LINK)
        )


