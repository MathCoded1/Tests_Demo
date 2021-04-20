from selenium import webdriver
import configparser


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.conf = configparser.ConfigParser()
        self.conf.read('Utilities/properties.ini')

    def getDriver(self):
        return self.driver

    def getConf(self):
        return self.conf


