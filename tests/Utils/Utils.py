__author__ = 'popka'

import os
from tests.Pages.AuthPage import AuthPage
from tests.Pages.CreatePage import CreatePage
from selenium.webdriver.support.ui import WebDriverWait

def auth(driver):
    USERNAME = 'tech-testing-ha2-14@bk.ru'
    PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'
    PH_USER = '#PH_user-email'

    auth_page = AuthPage(driver)
    auth_page.open()

    auth_form = auth_page.form
    auth_form.set_domain(DOMAIN)
    auth_form.set_login(USERNAME)
    auth_form.set_password(PASSWORD)
    auth_form.submit()

    create_page = CreatePage(driver)
    create_page.open()

    WebDriverWait(driver, 30, 0.1).until( #Wait for this page
            lambda d: d.find_element_by_css_selector(PH_USER).text
    )

    return create_page


