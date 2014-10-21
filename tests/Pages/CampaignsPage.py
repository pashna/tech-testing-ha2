__author__ = 'popka'
from selenium.webdriver.support.wait import WebDriverWait
from tests.Pages.Component import Component
from tests.Pages.Page import Page

class CampaignsPage(Page):

    PATH = '/ads/campaigns'
    @property
    def central_part(self):
        return CentralPart(self.driver)



class CentralPart(Component):
    CENTRAL_PART = '.campaigns-page__center-part'
    FIRST_ADS = '.control_stopped > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)'

    def get_page_source(self):
        element = self.driver.find_element_by_css_selector(self.CENTRAL_PART)
        return element.get_attribute("innerHTML")

    def open_edit_first_ads(self):
        self.driver.find_element_by_css_selector(self.FIRST_ADS).click()




