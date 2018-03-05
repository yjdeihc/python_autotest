#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest,time
from public.open import open_homepage
from public.login import login
class Message(unittest.TestCase):
    print(u"""系统消息""")

    @classmethod
    def setUpClass(self):
        open_homepage(self)
        request=login(self)
        self.webdriver=self.driver

        self.webdriver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        self.webdriver.find_element_by_id("main_navigation_system_message").click()


    def test_a_symessage(self):

        for i in range(30):
            try:
                if u"注册提醒" == self.webdriver.find_element_by_css_selector("div.ivu-table-cell.ivu-table-cell-ellipsis > div > span").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")


    def test_b_hasread(self):
        self.webdriver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
        self.webdriver.find_element_by_id("hasRead").click()


    def test_c_quiry(self):
        self.webdriver.find_element_by_xpath("//div[@id='title']/input").clear()
        self.webdriver.find_element_by_xpath("//div[@id='title']/input").send_keys(u"注册提醒")
        self.webdriver.find_element_by_id("search").click()
        for i in range(60):
            try:
                if u"注册提醒" == self.webdriver.find_element_by_css_selector("div.ivu-table-cell.ivu-table-cell-ellipsis > div > span").text: break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")

    def test_d_delete(self):
        self.webdriver.find_element_by_xpath("(//input[@type='checkbox'])[2]").click()
        self.webdriver.find_element_by_xpath("//button[@id='del']").click()
        self.webdriver.find_element_by_xpath("(//button[@type='button'])[9]").click()
        self.assertEqual(u"未能找到消息", self.webdriver.find_element_by_css_selector("h2").text)


    @classmethod
    def tearDownClass(self):
        self.webdriver.quit()



if __name__=="__main__":
    unittest.main()








