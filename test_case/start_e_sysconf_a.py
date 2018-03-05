#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest, time, re
import pymysql
from selenium import  webdriver
from public.open import  open_homepage
from public.login import login
from public.quit import quit
from public.getredis import *
from public.getmysql import *
from public.check_msg import chk_msg
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class personaldata(unittest.TestCase):
    print (u"""个人资料修改""")
    def test_a_update_username_sex(self):
        open_homepage(self)
        driver = self.driver
        login(self)
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_profile").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//div[@id='userprofile_info_name']/input").clear()
        driver.find_element_by_xpath("//div[@id='userprofile_info_name']/input").send_keys(u"这就是我的真实姓名")
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='userprofile_sex']/div/i[2]").click()
        time.sleep(2)
        driver.find_element_by_id("userprofile_sex_man").click()
        time.sleep(1)
        driver.find_element_by_id("userprofile_info_save").click()
        msg_text=u"更新个人资料成功"
        chk_msg(self,msg_text)





    def test_b_chang_pwd(self):
        open_homepage(self)
        requst = login(self)
        #passwordmd5='RNqbeGeD9GVLiSj3/J4b9MDF$dFXY0/jsYom8ehysg006T69Mimpm3crDnfmfB9I1Yls='
        passwordmd5='yEmTu+yT0VVEB6xOdZnGp3x/$5QY6GCt7PIxLEpIHqSTPSZNS/RCOQAybLg11wUPHuHw='
        #passwordmd5='OkDK/+Myx6lueyGvhFrI5Iac$Y1nPHwhfgl2lmz1fveVZim0lpNfHs5VNwz6xRLfDBC4='
        username = requst[0]
        phone_num = username
        passwd = requst[1]
        newpasswd='123456a'
        driver = self.driver
        driver.implicitly_wait
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_profile").click()
        driver.implicitly_wait(30)
        driver.find_element_by_id("userprofile_password_change").click()
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(passwd)
        driver.find_element_by_xpath("//div[@id='userprofile_password_change_new']/input").clear()
        driver.find_element_by_xpath("//div[@id='userprofile_password_change_new']/input").send_keys(newpasswd)
        driver.find_element_by_xpath("//div[@id='userprofile_password_change_new_confirm']/input").clear()
        driver.find_element_by_xpath("//div[@id='userprofile_password_change_new_confirm']/input").send_keys(newpasswd)
        driver.find_element_by_id("userprofile_password_change_sms_send").click()
        time.sleep(5)
        Random_code = selcet_chg_pwd (phone_num)
        Random_code = bytes.decode(Random_code)
        print (Random_code)
        driver.find_element_by_xpath("//div[@id='userprofile_password_change_sms_code']/input").clear()
        driver.find_element_by_xpath("//div[@id='userprofile_password_change_sms_code']/input").send_keys(Random_code)
        driver.find_element_by_id("userprofile_password_change_save").click()

        updat_sql="UPDATE ent_user SET password = '"+passwordmd5+"' WHERE mobile='"+phone_num+"'"
        update_p(sql=updat_sql)

        msg_text=u"更新账户密码成功"
        chk_msg(self,msg_text)

        user_idsql="SELECT id FROM  ent_user where  mobile='"+phone_num+"'"
        userid = get_id(sql=user_idsql)
        print(userid)
        delete_cache(userid)




    def test_chang_phone_num(self):
        open_homepage(self)
        requst = login(self)
        username = requst[0]
        phone_num = username
        newphone_num='15881015817'
        driver = self.driver
        driver.implicitly_wait
        driver.find_element_by_css_selector("div.ivu-menu-submenu-title").click()
        driver.find_element_by_id("main_navigation_system_profile").click()
        driver.implicitly_wait(30)
        driver.find_element_by_id("userprofile_phone_change").click()
        driver.find_element_by_id("userprofile_phone_change_sms_send").click()
        time.sleep(5)
        Random_code = selcet_chg_mobile (phone_num)
        Random_code = bytes.decode(Random_code)
        print (Random_code)
        driver.find_element_by_xpath("//div[@id='userprofile_phone_change_current_sms_code']/input").clear()
        driver.find_element_by_xpath("//div[@id='userprofile_phone_change_current_sms_code']/input").send_keys(Random_code)
        driver.find_element_by_id("userprofile_phone_change_next").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='userprofile_phone_change_new']/input").clear()
        driver.find_element_by_xpath("//div[@id='userprofile_phone_change_new']/input").send_keys(newphone_num)
        driver.find_element_by_id("userprofile_phone_change_new_sms_send").click()
        time.sleep(5)
        print(u"获取新号码的验证码")
        Random_code = selcet_chg_mobile (newphone_num)
        Random_code = bytes.decode(Random_code)
        print (Random_code)
        driver.find_element_by_xpath("//div[@id='userprofile_phone_change_new_sms_code']/input").clear()
        driver.find_element_by_xpath("//div[@id='userprofile_phone_change_new_sms_code']/input").send_keys(Random_code)
        driver.find_element_by_id("userprofile_phone_change_save").click()

        updat_sql="UPDATE ent_user SET mobile = '"+phone_num+"' WHERE mobile='"+newphone_num+"'"
        update_p(sql=updat_sql)

        user_idsql="SELECT id FROM  ent_user where  mobile='"+phone_num+"'"
        userid = get_id(sql=user_idsql)
        print(userid)
        delete_cache(userid)


        msg_text=u"新手机号绑定成功"
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



