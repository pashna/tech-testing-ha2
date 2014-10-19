import unittest
import tests
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from tests.Utils.Utils import auth

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            #desired_capabilities=getattr(DesiredCapabilities, browser).copy()
            desired_capabilities=DesiredCapabilities.FIREFOX.copy()
        )

    def test(self):
        auth(self.driver)



