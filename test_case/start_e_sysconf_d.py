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

class user_manage(unittest.TestCase):
    print (u"""用户管理""")
    def test_a_add_user(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        code = random.randint(1000,9999)
        code = str(code)
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_employees").click()
        driver.implicitly_wait(30)
        driver.find_element_by_id("system_employeesetting_btn_adduser").click()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_name']/input").send_keys(u"测试用户"+code)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_sex']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_sex']/div[2]/ul[2]/li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_roleid']/div/i[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_roleid']/div[2]/ul[2]/li[1]").click()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_mobile']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_mobile']/input").send_keys("1380013"+code)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_employeecode']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_employeecode']/input").send_keys(code)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_email']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_email']/input").send_keys(code+"@qq.com")
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_title']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_title']/input").send_keys(u"只是一个牛逼的职位")
        driver.find_element_by_id("system_employeesetting_btn_send_pwd").click()
        msg_text=u"添加用户成功"
        chk_msg(self,msg_text)

    def test_b_on_off_user(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_employees").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_table_userlist']/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button[3]").click()

        msg_text=u"禁用员工账户成功"
        chk_msg(self,msg_text)

        time.sleep(5)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_table_userlist']/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button[3]").click()
        msg_text=u"激活员工账户成功"
        chk_msg(self,msg_text)
        time.sleep(2)

    def test_c_eidt_user(self):
        open_homepage(self)
        login(self)
        driver = self.driver
        code = random.randint(1000,9999)
        code = str(code)
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_employees").click()
        driver.implicitly_wait(30)
        #driver.find_element_by_id("system_employeesetting_btn_adduser").click()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_table_userlist']/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button[2]").click()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_name']/input").send_keys(u"测试用户"+code)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_sex']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_sex']/div[2]/ul[2]/li[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_roleid']/div/i[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_roleid']/div[2]/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_employeecode']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_employeecode']/input").send_keys(code)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_email']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_email']/input").send_keys(code+"@qq.com")
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_title']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_title']/input").send_keys(u"只是一个牛逼的职位")
        driver.find_element_by_id("system_employeesetting_btn_submit").click()
        msg_text=u"编辑用户信息成功"
        chk_msg(self,msg_text)


    def test_d_eidt_user_pwd(self):
        open_homepage(self)
        login(self)
        driver = self.driver
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_employees").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[@id='system_employeesetting_table_userlist']/div/div[2]/table/tbody/tr[1]/td[5]/div/div/button[2]").click()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_password']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_employeesetting_input_password']/input").send_keys("123456")
        driver.find_element_by_id("system_employeesetting_btn_send_pwd").click()
        msg_text=u"修改用户密码成功"
        chk_msg(self,msg_text)
        time.sleep(3)

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
