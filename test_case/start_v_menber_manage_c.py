#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest, time, re
from public.open import  open_homepage
from public.login import login
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
import random

class member_template(unittest.TestCase):
    print (u"""短信模板管理""")
    def test_a_add(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
        driver.find_element_by_id("main_navigation_member_template").click()
        time.sleep(2)
        for i in range(10):
            try:
                if u"还没有短信模板" == driver.find_element_by_css_selector("h2").text:
                    status=1
                    print(status)
                    print(u"还没有短信模板")
                    break
            except: pass
            time.sleep(1)
        else:
            print(u"已经有短信模板")

        print(status)
        if (status==1):
            print(u"中间按钮")
            driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        else:
            print(u"点击顶部按钮")
            driver.find_element_by_id("member_template_btn_add").click()

        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='member_template_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='member_template_input_name']/input").send_keys(u"生日祝福短信"+code)
        driver.find_element_by_xpath("//div[@id='member_template_input_sign']/input").clear()
        driver.find_element_by_xpath("//div[@id='member_template_input_sign']/input").send_keys(u"短信签名信息"+code)
        driver.find_element_by_xpath("//div[@id='member_template_input_smsList']/textarea").clear()
        driver.find_element_by_xpath("//div[@id='member_template_input_smsList']/textarea").send_keys(u"祝你生日快乐"+code)
        driver.find_element_by_id("member_template_btn_save").click()


    def test_b_edit(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
        driver.find_element_by_id("main_navigation_member_template").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='member_template_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='member_template_input_name']/input").send_keys(u"生日祝福短信"+code)
        driver.find_element_by_xpath("//div[@id='member_template_input_sign']/input").clear()
        driver.find_element_by_xpath("//div[@id='member_template_input_sign']/input").send_keys(u"短信签名信息"+code)
        driver.find_element_by_xpath("//div[@id='member_template_input_smsList']/textarea").clear()
        driver.find_element_by_xpath("//div[@id='member_template_input_smsList']/textarea").send_keys(u"祝你生日快乐"+code)
        driver.find_element_by_id("member_template_btn_save").click()
    #
    def test_c_delete(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
        time.sleep(2)
        driver.find_element_by_id("main_navigation_member_template").click()
        time.sleep(2)
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//div[3]/button[2]").click()
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
