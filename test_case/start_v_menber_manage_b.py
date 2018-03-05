#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest, time, re
from public.open import  open_homepage
from public.login import login
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
import random

class member_labes(unittest.TestCase):
    print (u"""会员标签管理""")
    def test_a_add(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
        driver.find_element_by_id("main_navigation_member_labels").click()
        time.sleep(2)
        for i in range(10):
            try:
                if u"还没有标签" == driver.find_element_by_xpath("//div[@id='member_labels_list_error']/h2").text:
                    status=1
                    print(status)
                    print(u"还没有标签")
                    break
            except: pass
            time.sleep(1)
        else:
            print(u"已经有标签")

        print(status)
        if (status==1):
            print(u"中间按钮")
            driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        else:
            print(u"点击顶部按钮")
            driver.find_element_by_id("member_labels_btn_add").click()

        time.sleep(5)


        # driver.find_element_by_xpath("//div[@id='member_labels_input_name']/input").clear()
        # driver.find_element_by_xpath("//div[@id='member_labels_input_name']/input").send_keys(u"标签名字")
        # time.sleep(2)
        # driver.find_element_by_css_selector("div.ivu-btn-group > button.ivu-btn").click()
        # driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td/div/div/div/i[2]").click()
        # driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td/div/div/div[2]/ul[2]/li").click()
        # driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[2]/div/div/div/i[2]").click()
        # driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[2]/div/div/div[2]/ul[2]/li[2]").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[3]/div/div/div[2]/div/div[2]/div/div/i").click()
        # driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
        # driver.find_element_by_id("member_labels_btn_save_label").click()

        driver.find_element_by_xpath("//div[@id='member_labels_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='member_labels_input_name']/input").send_keys(u"标签名称")
        driver.find_element_by_css_selector("div.ivu-btn-group > button.ivu-btn").click()
        driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td/div/div/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td/div/div/div[2]/ul[2]/li[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[2]/div/div/div/span").click()
        driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[2]/div/div/div[2]/ul[2]/li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[3]/div/div/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[3]/div/div/div[2]/div/div/div/div[2]").click()
        driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[3]/div/div/div[2]/div/div[2]/div/div/i").click()
        time.sleep(2)
        driver.find_element_by_id("member_labels_btn_save_label").click()
    # #
    # def test_b_edit(self):
    #     open_homepage(self)
    #     requst = login(self)
    #     driver = self.driver
    #     status = 0
    #     code = random.randint(100,9999)
    #     code = str(code)
    #     driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li[4]/div").click()
    #     driver.find_element_by_id("main_navigation_member_labels").click()
    #     # driver.find_element_by_xpath("xpath=(//button[@type='button'])[6]").click()
    #     time.sleep(5)
    #     driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
    #     time.sleep(2)
    #     driver.find_element_by_xpath("//div[@id='member_labels_input_name']/input").clear()
    #     driver.find_element_by_xpath("//div[@id='member_labels_input_name']/input").send_keys(u"标签名字"+code)
    #     driver.find_element_by_css_selector("div.ivu-btn-group > button.ivu-btn").click()
    #     driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td/div/div/div/i[2]").click()
    #     driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td/div/div/div[2]/ul[2]/li").click()
    #     driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[2]/div/div/div/i[2]").click()
    #     driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[2]/div/div/div[2]/ul[2]/li[2]").click()
    #     driver.find_element_by_css_selector("div.selected").click()
    #     driver.find_element_by_css_selector("div.selected > i.ivu-icon.ivu-icon-android-checkbox-blank").click()
    #     driver.find_element_by_xpath("//div[@id='member_labels_table_rulelist']/div/div[2]/table/tbody/tr/td[3]/div/div/div[2]/div/div[2]/div/div/i").click()
    #     driver.find_element_by_xpath("(//input[@type='radio'])[2]").click()
    #     driver.find_element_by_id("member_labels_btn_save_label").click()
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
