# -*- coding: utf-8 -*-
import unittest, time, re,cgi,sys
import urllib
import requests
from  public.getsession import get_session

class get_dict_api(unittest.TestCase):
    print(u"""验证API基础字典表接口""")
    time.sleep(2)
    global host
    global _cookies
    global dictType
    dictType ='region'
    result = get_session()
    _cookies = result[0]
    host = result[1]
    print(_cookies)
    print(host)
    def test_get_from_id(self):
        import json
        id = '510100'
        name = '成都市'
        time.sleep(2)
        url = host+"/cbc/v1/system/dict/"+dictType+"/"+id
        req = requests.get(url=url,cookies=_cookies)
        print (url)
        resjson = req.json()
        json = json.dumps(resjson,ensure_ascii=False)
        print (u"判断",name,u"在返回的数据",json,u"中")
        if name in json:
            print (u"通过ID获取内容检查通过\n")
        else:
            print (u"通过ID获取内容检查失败\n")


    def test_get_from_pid(self):
        name = '成都市'
        pid='510000'
        time.sleep(3)
        url = host+"/cbc/v1/system/dict/"+dictType+"/"+pid+"/subs"
        req = requests.get(url=url,cookies=_cookies)
        json = req.json()["data"][0]["name"]
        print (u"判断",name,u"是否等于返回的数据",json)
        if name == json:
            print (u"通过PID获取子内容通过\n")
        else:
            print (u"通过PID获取子内容检查失败\n")


    def test_get_pid_is_null(self):
        name='北京市'
        url = host+"/cbc/v1/system/dict/"+dictType+"/_"+"/subs/"
        print (url)
        req = requests.get(url=url,cookies=_cookies)
        json = req.json()["data"][0]["name"]
        print (u"判断",name,u"是否等于返回的数据",json)
        if name == json:
            print (u"PID为空的时候获取顶级字典通过\n")
        else:
            print (u"PID为空的时候获取顶级字典失败\n")


    def test_get_search_name(self):
        name='阿坝藏族羌族自治州'
        urlname = urllib.parse.quote(name)
        url = host+"/cbc/v1/system/dict/"+dictType+"/search?name="+urlname
        print (url)
        req = requests.get(url=url,cookies=_cookies)
        json = req.json()["data"][0]["name"]
        print (u"判断",name,u"是否等于返回的数据",json)
        if name == json:
            print (u"模糊匹配字典接口验证通过\n")
        else:
            print (u"模糊匹配字典接口验证失败\n")





if __name__ == "__main__":
    unittest.main()