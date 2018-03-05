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

class enterprise(unittest.TestCase):
    print (u"""企业信息修改""")
    def test_a_update(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        code = random.randint(1000,9999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li/div/i[2]").click()
        driver.find_element_by_id("main_navigation_system_enterprise").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_name']/input").send_keys(u"企业名称"+code)
        # driver.find_element_by_css_selector("span.ivu-select-selected-value").click()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_modelprovince']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_modelprovince']/div[2]/ul[2]/li[13]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_modelcity']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_modelcity']/div[2]/ul[2]/li[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_enttype']/div/i[2]").click()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_enttype']/div[2]/ul[2]/li[2]").click()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_contactname']/input").clear()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_contactname']/input").send_keys(u"关云长"+code)
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_contactphone']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_contactphone']/input").send_keys("1380013"+code)
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_introduce']/textarea").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_introduce']/textarea").send_keys(u"这个企业很牛逼"+code)
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_valueweb']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_valueweb']/input").send_keys("http://www.baidu.com")
        driver.find_element_by_xpath("//button[@id='system_enterprise_companyinfo_button_createqr']").click()
        driver.find_element_by_xpath("//button[@id='system_enterprise_companyinfo_button_submit']").click()
        msg_text=u"企业信息保存成功"
        chk_msg(self,msg_text)

    def test_b_upload_logo(self):
        open_homepage(self)
        requst = login(self)
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li/div/i[2]").click()
        driver.find_element_by_id("main_navigation_system_enterprise").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_logo']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_companyinfo_input_logo']/input").send_keys("F:\\auto_test_qrb\\update\\00.jpg")

        time.sleep(2)

    def test_c_upload_certification(self):

        open_homepage(self)
        requst = login(self)
        username = requst[0]
        phone_num = username
        driver = self.driver
        code = random.randint(100000,999999)
        code = str(code)
        driver.find_element_by_xpath("//div[@id='app']/div/nav/ul/li/div/i[2]").click()
        driver.find_element_by_id("main_navigation_system_enterprise").click()
        driver.implicitly_wait(30)
        driver.find_element_by_id("system_enterprise_auth_button_showauthform").click()
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_name']/input").send_keys(u"牛逼的企业"+code)
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_bizlicense']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_bizlicense']/input").send_keys(code)
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_bizscope']/textarea").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_bizscope']/textarea").send_keys(u"啥都可以卖"+code)
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_legalperson']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_legalperson']/input").send_keys(u"张飞"+code)
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_addrinfo']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_addrinfo']/input").send_keys(u"三国杀"+code)
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_licence']/input").clear()
        driver.find_element_by_xpath("//div[@id='system_enterprise_auth_input_licence']/input").send_keys("F:\\auto_test_qrb\\update\\01.jpg")
        time.sleep(5)
        driver.find_element_by_id("system_enterprise_auth_button_submit").click()
        updata_sql= "UPDATE enterprise  SET approved =0 WHERE enterprise.id IN ( SELECT	ent_id FROM	ent_user	WHERE	mobile = '"+phone_num+"')"
        #print(updata_sql)
        update_p(sql=updata_sql)
        msg_text=u"认证信息提交成功"
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
