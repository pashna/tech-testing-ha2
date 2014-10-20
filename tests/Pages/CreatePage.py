#coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from tests.Pages.Component import Component
from tests.Pages.Page import Page
import os

#from tests.Utils.Utils import ajax_complete
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotVisibleException

__author__ = 'popka'


class CreatePage(Page):
    PATH = '/ads/create'
    MOBILE = '#product-type-6039'
    LENTA = '#pad-mobile_app_feed'
    SUBMIT = '.main-button-new'
    TITLE = '.base-setting__campaign-name__input'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def require_menu(self):
        return RequireMenu(self.driver)

    @property
    def age_restriction(self):
        return AgeRestriction(self.driver)

    def set_radio_mobile_app(self):
        self.driver.find_element_by_css_selector(self.MOBILE).click()

    def set_lenta(self):
        self.driver.find_element_by_css_selector(self.LENTA).click()

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()

    def set_title(self, title):
        element = self.driver.find_element_by_css_selector(self.TITLE)
        element.send_keys(title)

    def get_title(self):
        element = self.driver.find_element_by_css_selector(self.TITLE)
        return element.get_attribute("value")



class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class RequireMenu(Component):
    LINK = "/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[1]/span[2]/input"
    HEADER = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[2]/input'
    TEXT = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[3]/textarea'
    SMALL_PICTURE = '.banner-form__img-file'
    BIG_PICTURE = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[9]/form/div/input'
    TITLE = '.base-setting__campaign-name__input'

    def set_title(self, title):
        element = self.driver.find_element_by_css_selector(self.TITLE)
        element.send_keys(title)

    def set_link(self, link):
        link = unicode(link, errors='replace')
        element = self.driver.find_element_by_xpath(self.LINK)
        element.send_keys(link)

    def get_header(self):
        element = self.driver.find_element_by_xpath(self.HEADER)
        return element.get_attribute("value")

    def get_text(self):
        element = self.driver.find_element_by_xpath(self.TEXT)
        return element.get_attribute("value")

    def set_header(self, header):
        header = unicode(header, errors='replace')
        element = self.driver.find_element_by_xpath(self.HEADER)
        element.send_keys(header)

    def set_text(self, text):
        element = self.driver.find_element_by_xpath(self.TEXT)
        element.send_keys(text)

    def set_small_photo(self, path):
        absolute_path = os.path.abspath(path)
        element = self.driver.find_element_by_css_selector(self.SMALL_PICTURE)
        element.send_keys(absolute_path)

    def set_big_photo(self, path):
        absolute_path = os.path.abspath(path)
        element = self.driver.find_element_by_xpath(self.BIG_PICTURE)
        element.send_keys(absolute_path)


class AgeRestriction(Component):
    SIX = '//*[@id="restrict-6+"]'
    ZERO = '//*[@id="restrict-0+"]'
    TITLE = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[3]/div/div[2]/span'
    DEFAULT = '//*[@id="restrict-"]'

    def set_six(self):
        self.driver.find_element_by_xpath(self.SIX).click()

    def set_zero(self):
        self.driver.find_element_by_xpath(self.ZERO).click()

    def _set_default(self):
        self.driver.find_element_by_xpath(self.DEFAULT).click()

    def get_value(self):
        element = self.driver.find_element_by_xpath(self.TITLE)
        return element.get_attribute("innerHTML")

    def change_state(self):
        self.driver.find_element_by_xpath(self.TITLE).click()

    def close(self):
        element = self.driver.find_element_by_xpath(self.ZERO)
        if element.is_displayed():
            self._set_default()
            self.change_state()
        else:
            self.change_state()
            self._set_default()
            self.change_state()
