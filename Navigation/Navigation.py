from DriverStuff import DriverClass
from POMs import Login
from POMs import Login


class Navigate:
    def __init__(self):
        self.Drive = DriverClass.Driver()
        self.driver = self.Drive.getDriver()
        self.conf = self.Drive.getConf()
        self.Login = Login.Login()

    def goToLogin(self):
        self.driver.get(self.conf['URL']['base'])
