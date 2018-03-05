# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

def quit(self):
        driver = self.driver
        # driver.switch_to_default_content()
        #driver.find_element_by_class_name("navbar")
        time.sleep(4)
        driver.find_element_by_xpath("//button[@id='main_signout']").click()
        print  (u"退出登陆成功")