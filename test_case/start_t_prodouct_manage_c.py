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

class product_batch(unittest.TestCase):
    print (u"""批次管理""")
    def test_a_add(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[3]/div").click()
        driver.find_element_by_id("main_navigation_product_batch").click()
        for i in range(10):
            try:
                if u"还没有批次" == driver.find_element_by_xpath("//div[@id='product_batch_list_error_view']/h2").text:
                    status=1
                    break
            except: pass
            time.sleep(1)
        else:
            print(u"已经有批次")

        if (status==1):
            print(u"中间按钮")
            driver.find_element_by_xpath("//div[@id='product_batch_list_error_view']/button").click()
        else:
            print(u"点击顶部按钮")
            driver.find_element_by_id("product_batch_add").click()

        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='product_batch_edit_line_list']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_line_list']/div[2]/ul[2]/li").click()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_product_list']/div/span").click()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_product_list']/div[2]/ul[2]/li").click()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_no']/input").clear()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_no']/input").send_keys("201700001"+code)
        driver.find_element_by_id("product_batch_edit_submit").click()
        msg_text=u"更新批次成功"
        chk_msg(self,msg_text)
    #
    def test_b_edit(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[3]/div").click()
        driver.find_element_by_id("main_navigation_product_batch").click()
        time.sleep(20)
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_line_list']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_line_list']/div[2]/ul[2]/li").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='product_batch_edit_product_list']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_product_list']/div[2]/ul[2]/li").click()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_no']/input").clear()
        driver.find_element_by_xpath("//div[@id='product_batch_edit_no']/input").send_keys("201700001"+code)
        driver.find_element_by_id("product_batch_edit_submit").click()
        msg_text=u"更新批次成功"
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
    #     driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
    #     driver.find_element_by_css_selector("button.ivu-btn.ivu-btn-primary").click()
    #
    #
    #
    def test_d_delete(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[3]/div").click()
        driver.find_element_by_id("main_navigation_product_batch").click()
        time.sleep(20)
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[15]").click()
        msg_text=u"批次删除成功"
        chk_msg(self,msg_text)
        self.test_a_add()
    #
    # #
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
