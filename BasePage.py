from selenium import webdriver
from selenium.webdriver.common.by import By

#This is the base class that define attributes and methods to all classes

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.driver.timeout=30


#This class represents the login page that we have to create
class LoginPage(BasePage):
    email_id=(By.NAME,'email')
    pass_word=(By.NAME,'pass')
    submit_btn=(By.ID,'u_0_l')

    def set_email(self,email_id):
        email_element=self.driver.find_element(*LoginPage.email_id)
        email_element.send_keys(email_id)

    def set_password(self,password):
        password_element=self.driver.find_element(*LoginPage.pass_word)
        password_element.send_keys(password)

    def click_submit_btn(self):
        submit_button=self.driver.find_element(*LoginPage.submit_btn)
        submit_button.click()


    def login(self, email,password):
        self.set_email(email)
        self.set_password(password)
        self.click_submit_btn()
