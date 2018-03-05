# -*- coding: utf-8 -*-
import unittest, time, re,cgi,sys
import json
import requests


def get_session():
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        host = "http://www.test.com"
        url = host+"/cbc/v1/system/user/session"
        print (url)
        time.sleep(2)
        s = requests.Session()
        values = {'mobile': 17799999999,
                  'password': 123456}
        headerjson = {'Content-Type': 'application/json'}
        r = s.post(url=url, data = json.dumps(values),headers=headerjson)
        _cookies = r.cookies
        return _cookies,host






