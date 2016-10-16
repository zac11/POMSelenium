import unittest
import BasePage
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps=DesiredCapabilities.FIREFOX
caps['wires']=True

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Firefox(capabilities=caps)
        self.driver.get("https://www.facebook.com/")
    def test_login_incorrect_facebook(self):
        login_page=BasePage.LoginPage(self.driver)
        login_page.login('**************','***********')  #enter username and password here





    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
