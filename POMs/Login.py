from DriverStuff import DriverClass
import os


class Login:
    def __init__(self):
        self.driver = DriverClass.Driver().driver

    def getSignIn(self):
        return self.driver.find_element_by_link_text("Sign in")

    def clickSignIn(self):
        self.getSignIn().click()

    def getUsernameField(self):
        return self.driver.find_element_by_id('login_field')

    def getPasswordField(self):
        return self.driver.find_element_by_id('password')

    def enterUsername(self):
        self.getUsernameField().send_keys(os.getenv['GITHUB_USER'])

    def enterPassword(self):
        self.getPasswordField().send_keys(os.getenv['GITHUB_PASS'])

