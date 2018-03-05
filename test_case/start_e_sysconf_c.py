#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest, time, re
from public.open import  open_homepage
from public.login import login
from public.check_msg import chk_msg
from public.quit import quit
from public.getredis import *
from public.getmysql import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
import random

class payment(unittest.TestCase):
    print (u"""支付网关设置""")
    def test_a_set(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_payment").click()
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("button.ivu-btn.payment-list-edit-btn").click()
        driver.find_element_by_xpath("//div[@id='system_payment_setting_ctId']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_payment_setting_ctId']/input").send_keys("1234567890")
        driver.find_element_by_xpath("//div[@id='system_payment_setting_ctSecret']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_payment_setting_ctSecret']/input").send_keys("WIXJLGAXMGAOSFDASJDFASDFARGSDG")
        driver.find_element_by_xpath("//div[@id='system_payment_setting_AppId']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_payment_setting_AppId']/input").send_keys("99888")
        driver.find_element_by_xpath("//div[@id='system_payment_setting_AppSecret']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_payment_setting_AppSecret']/input").send_keys("99998888")
        driver.find_element_by_xpath("//div[@id='system_paymentsetting_wechat_cert_upload']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_paymentsetting_wechat_cert_upload']/input").send_keys("F:\\auto_test_qrb\\update\\sq.txt")
        driver.find_element_by_xpath("//div[@id='system_paymentsetting_wechat_oauth_upload']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_paymentsetting_wechat_oauth_upload']/input").send_keys("F:\\auto_test_qrb\\update\\sqzs.txt")
        driver.find_element_by_xpath("//button[@id='system_payment_setting_submit']").click()
        msg_text=u"支付网关更新成功"
        chk_msg(self,msg_text)

    def test_b_on_off(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_payment").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[@id='system_payment_setting_list']/div/div[2]/table/tbody/tr/td/div/div/span").click()
        msg_text=u"支付网关状态已设置为开启"
        chk_msg(self,msg_text)
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='system_payment_setting_list']/div/div[2]/table/tbody/tr/td/div/div/span").click()
        msg_text=u"支付网关状态已设置为关闭"
        chk_msg(self,msg_text)


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
