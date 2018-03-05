#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest, time, re
from public.open import  open_homepage
from public.login import login
from public.check_msg import chk_msg
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import random
import win32gui
import win32api
import win32con

class marketing_qrcode(unittest.TestCase):
    print (u"""二维码营销管理""")

    @classmethod
    def setUpClass(self):
        open_homepage(self)
        request = login(self)
        self.webdriver = self.driver
        self.webdriver.find_element_by_id("main_navigation_marketing").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("main_navigation_marketing_qrcode").click()


    def test_a_add_marketInfo(self):
        status = 0
        code = random.randint(100,9999)
        code = str(code)
        time.sleep(2)
        for i in range(10):
            try:
                if u"还没有营销活动" == self.webdriver.find_element_by_tag_name("h2").text:
                    status=1
                    print(status)
                    break
            except: pass
            time.sleep(1)
        else:
            print(u"已有营销活动")

        print(status)
        if (status==1):
            print(u"中间按钮,还没有营销活动")
            self.webdriver.find_element_by_id("app").find_elements_by_tag_name("button")[3].click()
        else:
            print(u"点击顶部按钮，已有营销活动")
            self.webdriver.find_element_by_id("marketing_qrcode_add").click()

        time.sleep(5)

        self.webdriver.find_element_by_xpath("//div[@id='marketing_qrcode_info_name']/input").clear()
        self.webdriver.find_element_by_xpath("//div[@id='marketing_qrcode_info_name']/input").send_keys(u"活动名称")
        self.webdriver.find_element_by_xpath("//div[@id='marketing_qrcode_info_title']/input").clear()
        self.webdriver.find_element_by_xpath("//div[@id='marketing_qrcode_info_title']/input").send_keys(u"活动标题")
        mindate_js = 'document.querySelectorAll("#marketing_qrcode_info_starttime input")[0].removeAttribute("readonly")'
        maxdate_js = 'document.querySelectorAll("#marketing_qrcode_info_endtime input")[0].removeAttribute("readonly")'
        self.webdriver.execute_script(mindate_js)
        self.webdriver.find_element_by_id("marketing_qrcode_info_starttime").find_element_by_tag_name("input").clear()
        self.webdriver.find_element_by_id("marketing_qrcode_info_starttime").find_element_by_tag_name("input").send_keys("2017/09/01 01:00:00")
        self.webdriver.find_element_by_id("marketing_qrcode_info_starttime").find_elements_by_tag_name("button")[1].click()
        self.webdriver.execute_script(maxdate_js)
        self.webdriver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        self.webdriver.find_element_by_id("marketing_qrcode_info_endtime").find_element_by_tag_name("input").clear()
        self.webdriver.find_element_by_id("marketing_qrcode_info_endtime").find_element_by_tag_name("input").send_keys("2017/09/30 01:00:00")
        self.webdriver.find_element_by_id("marketing_qrcode_info_endtime").find_elements_by_tag_name("button")[1].click()
        self.webdriver.find_element_by_xpath("//div[@id='marketing_qrcode_info_description']/textarea").clear()
        self.webdriver.find_element_by_xpath("//div[@id='marketing_qrcode_info_description']/textarea").send_keys(u"活动备注")
        self.webdriver.find_element_by_id("marketing_qrcode_info_template").click()
        self.webdriver.find_elements_by_class_name("global-dialog")[0].find_elements_by_tag_name("button")[1].click()
        self.webdriver.find_element_by_id("marketing_qrcode_info_product_add").click()
        self.webdriver.find_element_by_id("marketing_qrcode_info_product_source").find_elements_by_tag_name("input")[0].click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_info_product_selection_add").click()
        self.webdriver.find_element_by_id("marketing_qrcode_info_save").click()


    # def test_b_add_marketRundown(self):
    #     self.webdriver.find_element_by_xpath("//div[@id='marketing_qrcode_list']/div/div[2]/table/tbody/tr/td[3]/div/div/button[3]").click()
    #     time.sleep(2)
    #     self.webdriver.find_element_by_id("marketing_qrcode_info_next").click()
    #     time.sleep(3)
    #     market_methods = self.webdriver.find_element_by_id("marketing_qrcode_flow_events").find_elements_by_css_selector("[class='ivu-col ivu-col-span-12']")
    #     for button in market_methods:
    #         button.click()
    #         time.sleep(1)
    #     market_rundown = self.webdriver.find_element_by_id("marketing_qrcode_flow_tools").find_elements_by_css_selector ("[class='ivu-col ivu-col-span-12']")
    #     for button in market_rundown:
    #         button.click()
    #         time.sleep(1)
    #     self.webdriver.find_element_by_id("marketing_qrcode_flow_save").click()

<<<<<<< .mine
    def test_c_add_marketWelcome(self):
        time.sleep(2)
        self.webdriver.find_element_by_xpath(
            "//div[@id='marketing_qrcode_list']/div/div[2]/table/tbody/tr/td[3]/div/div/button[3]").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_info_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_flow_next").click()
||||||| .r6361
    def test_c_add_marketWelcome(self):
        self.webdriver.find_element_by_xpath(
            "//div[@id='marketing_qrcode_list']/div/div[2]/table/tbody/tr/td[3]/div/div/button[3]").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_info_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_flow_next").click()
=======
    # def test_c_add_marketWelcome(self):
    #     self.webdriver.find_element_by_xpath(
    #         "//div[@id='marketing_qrcode_list']/div/div[2]/table/tbody/tr/td[3]/div/div/button[3]").click()
    #     time.sleep(2)
    #     self.webdriver.find_element_by_id("marketing_qrcode_info_next").click()
    #     time.sleep(2)
    #     self.webdriver.find_element_by_id("marketing_qrcode_flow_next").click()
    #
    #     time.sleep(5)
    #     self.webdriver.find_element_by_tag_name("form").find_elements_by_css_selector("[class='upload-item js-add-file']")[0].click()
    #     dialog=win32gui.FindWindow('#32770',u'文件上传')
    #     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #     ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    #     Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    #     button = win32gui.FindWindowEx(dialog, 0, 'Button', u'打开')
    #     win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'E:\\QRcode\\resources\\a.png')
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    #     backcolor_js = 'document.getElementsByTagName("form")[0].getElementsByClassName("ivu-input")[0].removeAttribute("readonly")'
    #     self.webdriver.execute_js(backcolor_js)
    #     backcolor =
>>>>>>> .r6548
        time.sleep(5)

<<<<<<< .mine
        # upload background img
        start = time.time()
        self.uploadimg("[class='upload-item js-add-file']", 0)
        end = time.time()
        print("1time{}".format(end-start))
        time.sleep(30)

        # input background color
        backcolor_js = 'document.getElementsByTagName("form")[0].getElementsByClassName("ivu-input")[0].removeAttribute("readonly")'
        self.webdriver.execute_script(backcolor_js)
        self.webdriver.find_element_by_tag_name("form").find_elements_by_css_selector("[class='ivu-input']")[0].clear()
        self.webdriver.find_element_by_tag_name("form").find_elements_by_css_selector("[class='ivu-input']")[0].send_keys("#000000")
        time.sleep(5)
||||||| .r6361
        time.sleep(5)
        self.webdriver.find_element_by_tag_name("form").find_elements_by_css_selector("[class='upload-item js-add-file']")[0].click()
        dialog=win32gui.FindWindow('#32770',u'文件上传')
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', u'打开')
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'E:\\QRcode\\resources\\a.png')
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        backcolor_js = 'document.getElementsByTagName("form")[0].getElementsByClassName("ivu-input")[0].removeAttribute("readonly")'
        self.webdriver.execute_js(backcolor_js)
        backcolor =
=======
>>>>>>> .r6548

        # get title height slider
        # scroll the scroll bar until find the background color input, then we can drag and drop the title height slider
        # drag and drop the slider to the coordinate
        slider = self.webdriver.find_elements_by_class_name("ivu-slider-button")[0]
        js = "document.getElementsByTagName('form')[0].getElementsByClassName('ivu-input')[0].scrollIntoView()"
        self.webdriver.execute_script(js)
        actions = ActionChains(self.webdriver)
        actions.drag_and_drop_by_offset(slider,900,0).perform()
        time.sleep(5)

        # upload second background img
        start = time.time()
        self.uploadimg("[class='upload-item js-add-file']", 1)
        end = time.time()
        print("2time{}".format(end - start))
        time.sleep(30)




        # Get text slider
        # Invoke ActionChains Object
        # Drag and drop the slider to coordinate
        slider1 = self.webdriver.find_elements_by_class_name("ivu-slider-button")[1]
        print(slider1)
        actions = ActionChains(self.webdriver)
        actions.click_and_hold(slider1).perform()
        actions.drag_and_drop_by_offset(slider1, 1300, 0).perform()
        time.sleep(5)

<<<<<<< .mine
        # Remove "readonly" attribute from text color input
        js = 'document.getElementsByTagName("form")[0].getElementsByClassName("ivu-input")[1].removeAttribute("readonly")'
        self.webdriver.execute_script(js)
        self.webdriver.find_element_by_tag_name("form").find_elements_by_css_selector("[class='ivu-input']")[1].clear()
        self.webdriver.find_element_by_tag_name("form").find_elements_by_css_selector("[class='ivu-input']")[1].send_keys(Keys.CONTROL,
                                                                                                         'a')
        self.webdriver.find_element_by_tag_name("form").find_elements_by_css_selector("[class='ivu-input']")[1].send_keys(Keys.BACKSPACE,
                                                                                                                 "#FFFFFF")

||||||| .r6361

=======
>>>>>>> .r6548

        # iframe
        iframe = self.webdriver.find_element_by_tag_name("iframe")
        self.webdriver.switch_to_frame(iframe)
        self.webdriver.find_element_by_tag_name("body").send_keys("活动说明")
        self.webdriver.switch_to_default_content()
        time.sleep(5)



        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        time.sleep(2)

        # Footer height slider
        slider2 = self.webdriver.find_elements_by_class_name("ivu-slider-button")[2]
        print(slider2)
        actions = ActionChains(self.webdriver)
        actions.click_and_hold(slider2).perform()
        actions.drag_and_drop_by_offset(slider2, 1300, 0).perform()
        time.sleep(5)


        # upload third background img
        start = time.time()
        self.uploadimg("[class='upload-item js-add-file']", 2)
        end = time.time()
        print("3time{}".format(end - start))
        time.sleep(60)

    def test_d_add_swapnsend(self):
        time.sleep(2)
        self.webdriver.find_element_by_xpath(
            "//div[@id='marketing_qrcode_list']/div/div[2]/table/tbody/tr/td[3]/div/div/button[3]").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_info_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_flow_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        self.webdriver.find_element_by_id("market_qrcode_welcome_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_css_selector("#market_qrcode_gift_prize .ivu-select-selection").click() #点击奖品类别
        self.webdriver.find_elements_by_css_selector("#market_qrcode_gift_prize .ivu-select-dropdown-list li")[1].click() #在下拉框中选择红包
        self.webdriver.find_element_by_css_selector("#market_qrcode_gift_prize .ivu-row:nth-child(3) tr.ivu-table-row").click() #在表格中选中红包
        #self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        input = self.webdriver.find_elements_by_css_selector("#market_qrcode_gift_prize .ivu-row:nth-child(3) .ivu-input-number-input")[0] #获取数量输入框
        input.send_keys(Keys.CONTROL, 'a')
        input.send_keys(Keys.BACKSPACE, '10')
        self.webdriver.find_element_by_id("market_qrcode_gift_save").click()

    def test_e_add_lottery1(self):
        time.sleep(2)
        self.webdriver.find_element_by_xpath(
            "//div[@id='marketing_qrcode_list']/div/div[2]/table/tbody/tr/td[3]/div/div/button[3]").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_info_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_flow_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        self.webdriver.find_element_by_id("market_qrcode_welcome_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("market_qrcode_gift_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("market_lottery_award_button_add").click()
        self.webdriver.find_element_by_css_selector("#market_lottery_form_input_awardName input").send_keys(u"一等奖")# 输入奖项
        lottery_people = self.webdriver.find_element_by_css_selector("#market_lottery_form_input_lotteryMax input")# 定位到最大中奖人数
        lottery_people.send_keys(Keys.CONTROL, 'a')
        lottery_people.send_keys(Keys.BACKSPACE, '100')
        self.webdriver.find_element_by_css_selector("form >form .ivu-select").click() # 点击奖品类别
        self.webdriver.find_element_by_css_selector("form >form .ivu-select .ivu-select-item:nth-child(2)").click() # 在下拉框中选中红包
        self.webdriver.find_element_by_css_selector("form >form .ivu-row:nth-child(3) td:nth-child(2").click()# 在列表中选择红包
        prize_count = self.webdriver.find_element_by_css_selector("form >form .ivu-row:nth-child(3) .ivu-input-number-input")# 定位到中奖数量
        prize_count.send_keys(Keys.CONTROL, 'a')
        prize_count.send_keys(Keys.BACKSPACE, '100')
        self.webdriver.find_element_by_id("market_lottery_form_button_submit").click()
        self.webdriver.find_element_by_id("market_lottery_award_button_add").click()
        self.webdriver.find_element_by_css_selector("#market_lottery_form_input_awardName input").send_keys(
            u"二等奖")  # 输入奖项
        lottery_people = self.webdriver.find_element_by_css_selector(
            "#market_lottery_form_input_lotteryMax input")  # 定位到最大中奖人数
        lottery_people.send_keys(Keys.CONTROL, 'a')
        lottery_people.send_keys(Keys.BACKSPACE, '1000')
        self.webdriver.find_element_by_css_selector("form >form .ivu-select").click()  # 点击奖品类别
        self.webdriver.find_element_by_css_selector(
            "form >form .ivu-select .ivu-select-item:nth-child(2)").click()  # 在下拉框中选中红包
        self.webdriver.find_element_by_css_selector(
            "form >form .ivu-row:nth-child(3) td:nth-child(2").click()  # 在列表中选择红包
        prize_count = self.webdriver.find_element_by_css_selector(
            "form >form .ivu-row:nth-child(3) .ivu-input-number-input")  # 定位到中奖数量
        prize_count.send_keys(Keys.CONTROL, 'a')
        prize_count.send_keys(Keys.BACKSPACE, '1000')
        self.webdriver.find_element_by_id("market_lottery_form_button_submit").click()
        self.webdriver.find_element_by_id("market_lottery_award_button_add").click()
        self.webdriver.find_element_by_css_selector("#market_lottery_form_input_awardName input").send_keys(
            u"三等奖")  # 输入奖项
        lottery_people = self.webdriver.find_element_by_css_selector(
            "#market_lottery_form_input_lotteryMax input")  # 定位到最大中奖人数
        lottery_people.send_keys(Keys.CONTROL, 'a')
        lottery_people.send_keys(Keys.BACKSPACE, '10000')
        self.webdriver.find_element_by_css_selector("form >form .ivu-select").click()  # 点击奖品类别
        self.webdriver.find_element_by_css_selector(
            "form >form .ivu-select .ivu-select-item:nth-child(2)").click()  # 在下拉框中选中红包
        self.webdriver.find_element_by_css_selector(
            "form >form .ivu-row:nth-child(3) td:nth-child(2").click()  # 在列表中选择红包
        prize_count = self.webdriver.find_element_by_css_selector(
            "form >form .ivu-row:nth-child(3) .ivu-input-number-input")  # 定位到中奖数量
        prize_count.send_keys(Keys.CONTROL, 'a')
        prize_count.send_keys(Keys.BACKSPACE, '10000')
        self.webdriver.find_element_by_id("market_lottery_form_button_submit").click()
        # 启用必中奖
        self.webdriver.find_element_by_css_selector("#market_lottery_award_checkbox_enableSpecAward input").click()
        # 选择抽奖方式
        self.webdriver.find_element_by_css_selector("#market_lottery_award_select_lotteryType").click()
        self.webdriver.find_element_by_css_selector("#market_lottery_award_select_lotteryType li:nth-child(2)").click()
        self.webdriver.find_element_by_id("market_lottery_award_button_next").click()

    def test_f_add_lottery2(self):
        time.sleep(2)
        self.webdriver.find_element_by_xpath(
            "//div[@id='marketing_qrcode_list']/div/div[2]/table/tbody/tr/td[3]/div/div/button[3]").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_info_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_flow_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        self.webdriver.find_element_by_id("market_qrcode_welcome_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("market_qrcode_gift_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("market_lottery_award_button_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("market_lottery_page_button_save").click()

    def test_g_add_xxx(self):
        time.sleep(2)
        self.webdriver.find_element_by_xpath(
            "//div[@id='marketing_qrcode_list']/div/div[2]/table/tbody/tr/td[3]/div/div/button[3]").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_info_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_id("marketing_qrcode_flow_next").click()
        time.sleep(2)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        self.webdriver.find_element_by_tag_name("html").send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        self.webdriver.find_element_by_id("market_qrcode_welcome_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("market_qrcode_gift_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("market_lottery_award_button_next").click()
        time.sleep(5)
        self.webdriver.find_element_by_id("market_lottery_page_button_next").click()










    def uploadimg(self,locator,i):
        self.webdriver.find_element_by_tag_name("form").find_elements_by_css_selector(
            locator)[i].click()
        #dialog = win32gui.FindWindow('#32770', u'文件上传') # Firefox
        dialog = win32gui.FindWindow('#32770', u'打开')  # Chrome
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', u'打开(&O)')
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'E:\\QRcode\\update\\a.png')
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)


if __name__ == "__main__":
    unittest.main()
    #marketing_qrcode().uploadimg("[class='upload-item js-add-file']", 2)
