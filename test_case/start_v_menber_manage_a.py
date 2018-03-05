#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest, time, re
from public.open import  open_homepage
from public.login import login
from public.check_msg import chk_msg
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random

class member_levels(unittest.TestCase):
    print (u"""会员等级管理""")
    def test_a_add(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
        driver.find_element_by_id("main_navigation_member_levels").click()
        time.sleep(2)
        for i in range(10):
            try:
                if u"还没有等级" == driver.find_element_by_xpath("//div[@id='product_product_list_error']/h2").text:
                    status=1
                    print(status)
                    break
            except: pass
            time.sleep(1)
        else:
            print(u"已经有等级")

        print(status)
        if (status==1):
            print(u"中间按钮")
            driver.find_element_by_xpath("//div[@id='product_product_list_error']/button").click()
        else:
            print(u"点击顶部按钮")
            driver.find_element_by_id("member_levels_btn_add").click()

        time.sleep(5)
        driver.find_element_by_css_selector("input.ivu-input").clear()
        driver.find_element_by_css_selector("input.ivu-input").send_keys(u"铜牌会员"+code)
        driver.find_element_by_xpath("//div[@id='member_levels_radio_default']/label/span/input").click()
        driver.find_element_by_xpath("//div[@id='member_levels_radio_default']/label[2]/span/input").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div/div/div/div/div/span[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div/div/div/div/div[2]/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemin']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemin']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemin']/div[2]/input").send_keys(Keys.BACKSPACE, 1)
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemax']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemax']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemax']/div[2]/input").send_keys(Keys.BACKSPACE,999)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div/div/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div/div/div[2]/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmin']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmin']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmin']/div[2]/input").send_keys(Keys.BACKSPACE, 99)
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmax']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmax']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmax']/div[2]/input").send_keys(Keys.BACKSPACE, 999)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='member_levels_input_priority']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_input_priority']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_input_priority']/div[2]/input").send_keys(Keys.BACKSPACE, 20)
        driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_id("member_levels_btn_savelevel").click()
        msg_text=u"添加成功"
        chk_msg(self,msg_text)

    def test_b_edit(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
        driver.find_element_by_id("main_navigation_member_levels").click()
        #driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        time.sleep(10)
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        driver.find_element_by_css_selector("input.ivu-input").clear()
        driver.find_element_by_css_selector("input.ivu-input").send_keys(u"铜牌会员" + code)
        driver.find_element_by_xpath("//div[@id='member_levels_radio_default']/label/span/input").click()
        driver.find_element_by_xpath("//div[@id='member_levels_radio_default']/label[2]/span/input").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div/div/div/div/div/span[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div/div/div/div/div[2]/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemin']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemin']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemin']/div[2]/input").send_keys( Keys.BACKSPACE, 22)
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemax']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemax']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_timemax']/div[2]/input").send_keys(Keys.BACKSPACE, 222)
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmin']/div[2]/input").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div/div/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]/div[2]/div/div/div/div[2]/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmin']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmin']/div[2]/input").send_keys(Keys.BACKSPACE, 11)
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmax']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmax']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_numinput_mountmax']/div[2]/input").send_keys(Keys.BACKSPACE, 111)
        driver.find_element_by_xpath("//div[@id='member_levels_input_priority']/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='member_levels_input_priority']/div[2]/input").send_keys(Keys.CONTROL, 'a')
        driver.find_element_by_xpath("//div[@id='member_levels_input_priority']/div[2]/input").send_keys(Keys.BACKSPACE,20)
        driver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        driver.find_element_by_id("member_levels_btn_savelevel").click()
        msg_text = u"保存成功"
        chk_msg(self, msg_text)

    def test_c_edit(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
        driver.find_element_by_id("main_navigation_member_levels").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[11]").click()
        msg_text=u"会员等级重算成功"
        chk_msg(self,msg_text)

        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        msg_text=u"操作成功"
        chk_msg(self,msg_text)

    def test_d_delete(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
        driver.find_element_by_id("main_navigation_member_levels").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//button[@type='button'])[8]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
        self.test_a_add()


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
