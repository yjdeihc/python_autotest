# -*- coding: utf-8 -*-
import unittest, time, re,cgi,sys
import requests
from  public.getsession import get_session

class shorturl(unittest.TestCase):
    print (u"""验证API短地址接口""")
    global host
    global _cookies
    global shorturl
    global longurl
    longurl="http://ptcs.51s.co/system/enterprise"
    dictType ='region'
    result = get_session()
    _cookies = result[0]
    host = result[1]
    print(_cookies)
    print(host)


    def test_get_ashorturl_and_decode_shorturl_to_longurl(self):
        time.sleep(2)

        url=host+"/cbc/v1/system/shorturl/url?longurl="+longurl
        print(url)
        req = requests.get(url=url,cookies=_cookies)
        shorturl = req.json()["data"]
        r = shorturl
        shortcode = re.sub(r'^http://51s.com/',"",r)
        print (u"短地址URL是"+shortcode)

        url=host+shortcode
        print (url)
        r = requests.get(url,cookies=_cookies)
        print(r)
        # baklongurl = r.json()["data"]
        # print(baklongurl)
        # print (u"判断原URL",longurl,u"是否和返回的URL是否相等",baklongurl,u"")
        # if longurl == baklongurl:
        #     print (u"通过URL内容检查通过\n")
        # else:
        #     print (u"通过URL内容检查失败\n")

    def test_get_shorturl_from_uuid(self):
        time.sleep(2)
        UUID="0D6468C1-721E-CACA-436C-42C69A82ADCE"
        url=host+"/cbc/v1/system/shorturl/produrl/"+UUID
        print (url)
        r = requests.get(url,cookies=_cookies)
        resjson = r.json()["data"]
        shortcode = re.sub(r'^http://51s.com/',"",resjson)
        print (u"根据UUID生成的短地址URL是"+shortcode)
        if shortcode.isdigit():
            print (u"是纯数字")
        else:
            print (u"不是纯数字")
            if len(shortcode)==6:
                print (u"短地址长度检查通过")
            else:
                print (u"短地址长度检测不通过")




if __name__ == "__main__":
    unittest.main()