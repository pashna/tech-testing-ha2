__author__ = 'popka'

import os
from tests.Pages.AuthPage import AuthPage
from tests.Pages.CreatePage import CreatePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import random
import string

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

    wait_for_create_page_load(driver)

    return create_page

def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass

def wait_for_ajax_complete(driver):
    WebDriverWait(driver, 30, 3).until(ajax_complete, 'AJAX')


def wait_for_create_page_load(driver):
    LAST_ELEMENT = '/html/body/div[8]'
    WebDriverWait(driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(LAST_ELEMENT)
    )

def wait_for_campaigns_page_load(driver):
    LAST_ELEMENT = '/html/body/div[9]'
    WebDriverWait(driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(LAST_ELEMENT)
    )

def generate_random_word(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))


def fill_require(driver, create_page, LINK='play.google.com/store/apps/details?id=org.bmstu.BmstuSchedule&hl=ru',
                 HEADER = 'BMSTU DASHBOARD', TEXT = 'AMAZING APPLICATION! FOR YOU, FOR ME, FOR YOUR CAT',
                 BIG_PHOTO = 'banner.jpg', SMALL_PHOTO = 'icon.jpg', title = generate_random_word(5)):

    #create_page = auth(driver=driver)
    create_page.set_title(title)
    create_page.set_radio_mobile_app()
    create_page.set_lenta()

    require_menu = create_page.require_menu
    require_menu.set_link(LINK)
    wait_for_ajax_complete(driver=driver)

    require_menu.set_header(HEADER)
    require_menu.set_text(TEXT)
    require_menu.set_big_photo(BIG_PHOTO)
    require_menu.set_small_photo(SMALL_PHOTO)

    wait_for_ajax_complete(driver=driver)






