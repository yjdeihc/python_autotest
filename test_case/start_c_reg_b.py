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

class forgetpwd(unittest.TestCase):
    print (u"找回密码")

    def test_reset_pwd(self):
        open_homepage(self)
        phone_num='17799999999'
        passwd_num='123456'
        driver = self.driver
        driver.get(self.base_url + "/signin")
        time.sleep(80)
        # 因为同一个手机号一分钟之内只能发一条短信.这里需要等待注册的短信发送超过60秒后在发送忘记重置密码的短信
        driver.find_element_by_link_text(u"找回密码").click()
        print(u"点击找回密码")
        time.sleep(10)

        driver.find_element_by_xpath("//div[@id='resetPwd_account']/input").clear()
        driver.find_element_by_xpath("//div[@id='resetPwd_account']/input").send_keys(phone_num)
        driver.find_element_by_xpath("//div[@id='resetPwd_password']/input").clear()
        driver.find_element_by_xpath("//div[@id='resetPwd_password']/input").send_keys(passwd_num)
        driver.find_element_by_xpath("//div[@id='resetPwd_password_confirm']/input").clear()
        driver.find_element_by_xpath("//div[@id='resetPwd_password_confirm']/input").send_keys(passwd_num)
        driver.find_element_by_id("resetPwd_sendsms_btn").click()
        time.sleep(10)
        Random_code = selcet_chg_pwd (phone_num)
        Random_code = bytes.decode(Random_code)
        print (Random_code)
        driver.find_element_by_xpath("//div[@id='resetPwd_sms_code']/input").clear()
        driver.find_element_by_xpath("//div[@id='resetPwd_sms_code']/input").send_keys(Random_code)
        driver.find_element_by_id("resetPwd_btn").click()
        time.sleep(3)
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
