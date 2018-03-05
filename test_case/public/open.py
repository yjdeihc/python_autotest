# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import unittest, time, re

def open_homepage(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "https://ptwc.test.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        return self






