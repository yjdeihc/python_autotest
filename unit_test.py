#coding=utf-8
import unittest,time,os,datetime
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText



#发送邮件
def sentmail(filename):
    file_new=filename
    #发信邮箱
    mail_from='pms@erathink.com'
    #收信邮箱
    mail_to=['cwang@erathink.com','hbliu@erathink.com']
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=u"万码易联测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('smtp.qiye.163.com')
    #用户名密码
    smtp.login('pms@erathink.com','Pms20152015')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print ('email has send out !')


#获取测试用例
def get_case():
    result_dir = 'F:\\auto_test_qrb\\test_case'
    discover = unittest.defaultTestLoader.discover(result_dir,pattern ='start_up_per*.py',top_level_dir=None)
    #print (discover)
    return discover

# #生成测试结果的HTML
# def runAutomation():
#


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename="F:\\auto_test_qrb\\report\\"+now+'result.html'
    # print filename+'原始路径'
    html = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=html,title=u'测试报告',description=u'用例执行情况:')
    print (runner)
    runner.run(get_case())
    html.close()
    #sentmail(filename)



