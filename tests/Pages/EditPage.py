#coding=utf-8

__author__ = 'popka'
from selenium.webdriver.support.wait import WebDriverWait
from tests.Pages.Component import Component
from tests.Pages.Page import Page
import os

class EditPage(Page):
    PATH = '/ads/campaigns/'

    @property
    def interest_form(self):
        return ForForm(self.driver)

    @property
    def age_restriction_form(self):
        return AgeRestriction(self.driver)


class ForForm(Component):
    INTERST = '.campaign-setting__wrapper_interests > span:nth-child(1)'
    SELECTED_LIST = 'div.campaign-setting__tree-placeholder:nth-child(1) > div:nth-child(2) > ul:nth-child(2)'

    def open_interest(self):
        self.driver.find_element_by_css_selector(self.INTERST).click()

    def get_interest_value(self):
        elem = self.driver.find_element_by_css_selector(self.INTERST)
        return elem.get_attribute("innerHTML")

    def is_selected(self, array_name):
        select_list = self.driver.find_element_by_css_selector(self.SELECTED_LIST)
        source = select_list.get_attribute("innerHTML").encode('utf-8')
        print(source)
        if len(array_name) > 5:
            print('(' + str(len(array_name)) + ' из 12)')
            if ( '(' + str(len(array_name)) + ' из 12)' ) in source:
                return True
        else:
            for i in range(len(array_name)):
                if array_name[i] not in source:
                    return False
        return True


    def is_business_selected(self):
        business = "Бизнес"
        select_list = self.driver.find_element_by_css_selector(self.SELECTED_LIST)
        source = select_list.get_attribute("innerHTML").encode('utf-8')
        print(source)
        if business in source:
            return True
        else:
            return False



class AgeRestriction(Component):
    VALUE = '.campaign-setting__wrapper_restrict > span:nth-child(1)'

    def get_value(self):
        element = self.driver.find_element_by_css_selector(self.VALUE)
        return element.get_attribute("innerHTML")