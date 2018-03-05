# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

def chk_msg(self,msg_text):

        driver = self.driver
        #print(msg_text)
        for i in range(10):
            try:
                if msg_text in driver.find_element_by_css_selector("div.ivu-message-custom-content.ivu-message-success > span").text:
                        print(msg_text)
                        break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        time.sleep(5)