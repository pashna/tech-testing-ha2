#coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from tests.Pages.Component import Component
from tests.Pages.Page import Page
import os

#from tests.Utils.Utils import ajax_complete
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException

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







    # TRY TO MOVE INTO UTILS!!!!




