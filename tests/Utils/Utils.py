__author__ = 'popka'

import os
from tests.Pages.AuthPage import AuthPage
from tests.Pages.CreatePage import CreatePage

def auth(driver):
    USERNAME = 'tech-testing-ha2-14@bk.ru'
    PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'

    auth_page = AuthPage(driver)
    auth_page.open()

    auth_form = auth_page.form
    auth_form.set_domain(DOMAIN)
    auth_form.set_login(USERNAME)
    auth_form.set_password(PASSWORD)
    auth_form.submit()

    create_page = CreatePage(driver)
    create_page.open()


