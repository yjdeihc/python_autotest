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

class staric_code(unittest.TestCase):
    print (u"""静态二维码管理""")
    def test_a_add_code(self):
        open_homepage(self)
        requst = login(self)
        status = 3
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[2]/div").click()
        driver.find_element_by_id("main_navigation_qrcode_static").click()
        for i in range(30):
            try:
                if u"还没有静态码" == driver.find_element_by_xpath("//div[@id='system_employeesetting_list_error']/h2").text:
                    status =1
                    print(status)
                    break
            except:pass
            time.sleep(1)
        else:
            print(u"找到内容")

        if (status==1):
            print(u"中间按钮")
            driver.find_element_by_xpath("//div[@id='system_employeesetting_list_error']/button").click()
        else:
            print(u"点击顶部按钮")
            driver.find_element_by_id("qrcode_static_qrcodelist_creatQRcode").click()
        driver.find_element_by_xpath("//button[@id='qrcode_static_btn_texttype']").click()
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_textinput']/textarea").clear()
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_textinput']/textarea").send_keys(u"静态码")
        driver.find_element_by_xpath("//button[@id='qrcode_static_btn_webtype']").click()
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_webinput']/input").clear()
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_webinput']/input").send_keys("www.baidu.com")
        driver.find_element_by_id("qrcode_static_qrcodelist_saveqrcode").click()
        msg_text=u"新增内容成功"
        chk_msg(self,msg_text)

    def test_b_edit_code(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[2]/div").click()
        driver.find_element_by_id("main_navigation_qrcode_static").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_table']/div/div[2]/table/tbody/tr/td[2]/div/div/button").click()
        driver.find_element_by_id("qrcode_static_btn_texttype").click()
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_textinput']/textarea").clear()
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_textinput']/textarea").send_keys(u"文本内容就是我")
        driver.find_element_by_id("qrcode_static_btn_webtype").click()
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_webinput']/input").clear()
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_webinput']/input").send_keys("www.baiduyun.com")
        driver.find_element_by_id("qrcode_static_qrcodelist_saveqrcode").click()
        msg_text=u"编辑内容成功"
        chk_msg(self,msg_text)

    #
    # def test_c_list_code(self):
    #     open_homepage(self)
    #     requst = login(self)
    #     driver = self.driver
    #     driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[2]/div").click()
    #     driver.find_element_by_id("main_navigation_qrcode_static").click()
    #     time.sleep(10)
    #     driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_table']/div/div[2]/table/tbody/tr/td[2]/div/div/button[2]").click()
    #     driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
    #     driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
    #     driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
    #     driver.find_element_by_css_selector("button.ivu-btn.ivu-btn-primary").click()
    #


    def test_d_delete_code(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[2]/div").click()
        driver.find_element_by_id("main_navigation_qrcode_static").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_table']/div/div[2]/table/tbody/tr/td[2]/div/div/button[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[14]").click()
        msg_text=u"删除静态码成功"
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
