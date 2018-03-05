# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


def login(self,username = '17799999999',pwd='123456'):

        driver = self.driver
        driver.get(self.base_url + "/signin")
        time.sleep(10)
        driver.find_element_by_xpath("//div[@id='signin_account']/input").clear()
        driver.find_element_by_xpath("//div[@id='signin_account']/input").send_keys(username)
        driver.find_element_by_xpath("//div[@id='signin_password']/input").clear()
        driver.find_element_by_xpath("//div[@id='signin_password']/input").send_keys(pwd)
        driver.find_element_by_id("signin_btn").click()
        for i in range(10):
            try:
                if u"最新消息" == driver.find_element_by_css_selector("p").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        time.sleep(2)
        return username,pwd
