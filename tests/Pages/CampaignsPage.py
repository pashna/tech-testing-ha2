__author__ = 'popka'
from selenium.webdriver.support.wait import WebDriverWait
from tests.Pages.Component import Component
from tests.Pages.Page import Page

class CampaignsPage(Page):

    PATH = '/ads/campaigns'
    CENTRAL_PART = '.campaigns-page__center-part'

    def get_page_source(self):
        element = self.driver.find_element_by_css_selector(self.CENTRAL_PART)
        return element.get_attribute("innerHTML")



