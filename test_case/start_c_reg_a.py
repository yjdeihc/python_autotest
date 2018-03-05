# -*- coding: utf-8 -*-
import unittest, time, re
import random
from public.open import open_homepage
from public.quit import quit
from public.check_msg import chk_msg
from public.login import login
from public.getmysql import getconn
from public.getredis import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class Reg(unittest.TestCase):
    print (u"注册账号")

    def test_reg_user(self):
        open_homepage(self)
        phone_num='17799999999'
        code = random.randint(100,9999)
        code = str(code)
        enterprise_name = u"企业名称"+code
        print(enterprise_name)
        passwd_num='123456'
        get_phonecode_sql = phone_num
        del_user_sql = "delete FROM ent_user where mobile ='"+phone_num+"'"
        aaa = getconn(del_user_sql)
        print (aaa)
        driver = self.driver

        driver.get(self.base_url + "/signin")
        time.sleep(5)
        driver.find_element_by_link_text(u"免费注册").click()
        driver.find_element_by_xpath("//div[@id='signup_account']/input").clear()
        driver.find_element_by_xpath("//div[@id='signup_account']/input").send_keys(phone_num)
        driver.find_element_by_xpath("//div[@id='signup_ent_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='signup_ent_name']/input").send_keys(enterprise_name)
        driver.find_element_by_xpath("//div[@id='signup_password']/input").clear()
        driver.find_element_by_xpath("//div[@id='signup_password']/input").send_keys(passwd_num)
        driver.find_element_by_xpath("//div[@id='signup_password_confirm']/input").clear()
        driver.find_element_by_xpath("//div[@id='signup_password_confirm']/input").send_keys(passwd_num)
        driver.find_element_by_xpath("//div[@id='signup_sms_code']/div/button").click()
        time.sleep(10)
        Random_code = selcet_reg (get_phonecode_sql)
        Random_code = bytes.decode(Random_code)
        print (Random_code)
        driver.find_element_by_xpath("//div[@id='signup_sms_code']/input").clear()
        driver.find_element_by_xpath("//div[@id='signup_sms_code']/input").send_keys(Random_code)
        driver.find_element_by_xpath("//button[@id='signup_btn']").click()
        login(self)


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
