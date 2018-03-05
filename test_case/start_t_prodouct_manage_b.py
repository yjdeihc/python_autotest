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

class product(unittest.TestCase):
    print (u"""产品管理""")
    def test_a_add(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[3]/div").click()
        driver.find_element_by_id("main_navigation_product_management").click()
        for i in range(30):
            try:
                if u"还没有产品" == driver.find_element_by_xpath("//div[@id='product_product_list_error']/h2").text:
                    status=1
                    break
            except: pass
            time.sleep(1)
        else:
            print(u"已经有产品")

        if (status==1):
            print(u"中间按钮")
            driver.find_element_by_xpath("//div[@id='product_product_list_error']/button").click()
        else:
            print(u"点击顶部按钮")
            driver.find_element_by_id("product_product_btn_addproduct").click()


        driver.find_element_by_xpath("//div[@id='product_addproduct_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_name']/input").send_keys(u"可爱多"+code)
        driver.find_element_by_xpath("//div[@id='product_addproduct_select_line']/div/span").click()
        driver.find_element_by_xpath("//div[@id='product_addproduct_select_line']/div[2]/ul[2]/li").click()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_units']/input").clear()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_units']/input").send_keys(u"东莞1厂"+code)
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_specification']/input").clear()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_specification']/input").send_keys(u"袋装"+code)
        driver.find_element_by_id("product_addproduct_btn_save").click()
        msg_text=u"添加成功"
        chk_msg(self,msg_text)

    def test_b_edit(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[3]/div").click()
        driver.find_element_by_id("main_navigation_product_management").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_name']/input").send_keys(u"可爱多"+code)
        driver.find_element_by_xpath("//div[@id='product_addproduct_select_line']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='product_addproduct_select_line']/div[2]/ul[2]/li").click()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_units']/input").clear()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_units']/input").send_keys(u"东莞1厂"+code)
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_specification']/input").clear()
        driver.find_element_by_xpath("//div[@id='product_addproduct_input_specification']/input").send_keys(u"袋装"+code)
        driver.find_element_by_id("product_addproduct_btn_save").click()
        msg_text=u"编辑成功"
        chk_msg(self,msg_text)
        driver.find_element_by_xpath("//input[@type='file']").clear()
        driver.find_element_by_xpath("//input[@type='file']").send_keys("F:\\auto_test_qrb\\update\\00.jpg")

    # #
    # # def test_c_list_code(self):
    # #     open_homepage(self)
    # #     requst = login(self)
    # #     driver = self.driver
    # #     driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[2]/div").click()
    # #     driver.find_element_by_id("main_navigation_qrcode_static").click()
    # #     time.sleep(10)
    # #     driver.find_element_by_xpath("//div[@id='qrcode_static_qrcodelist_table']/div/div[2]/table/tbody/tr/td[2]/div/div/button[2]").click()
    # #     driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
    # #     driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
    # #     driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
    # #     driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
    # #     driver.find_element_by_css_selector("button.ivu-btn.ivu-btn-primary").click()
    # #
    # #
    # #
    def test_d_delete(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[3]/div").click()
        driver.find_element_by_id("main_navigation_product_management").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[12]").click()
        msg_text=u"删除产品成功"
        chk_msg(self,msg_text)
        self.test_a_add()

    #
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
