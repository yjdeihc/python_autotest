# public 模块的 __init__.py
# #coding=utf-8
import redis
import re



    #查询数据
def selcet_reg(get_phonecode_sql):
        sql=get_phonecode_sql
        r = redis.Redis(host='139.196.25.231',port=6379,db=3,password='root')
        print(sql)
        sql="REG_ENT-"+sql
        print(sql)
        value = r.get(sql)
        print(value)
        return value


def selcet_chg_pwd(phone_num):
        sql=phone_num
        r = redis.Redis(host='139.196.25.231',port=6379,db=3,password='root')
        print(sql)
        sql="CHG_PWD-"+sql
        print(sql)
        value = r.get(sql)
        print(value)
        return value


def selcet_chg_mobile(newphone_num):
        sql=newphone_num
        r = redis.Redis(host='139.196.25.231',port=6379,db=3,password='root')
        print(sql)
        sql="CHG_MOBILE-"+sql
        print(sql)
        value = r.get(sql)
        print(value)
        return value



def delete_cache(userid):
        r = redis.Redis(host='139.196.25.231',port=6379,db=3,password='root')
        print(userid)
        sql="EnterpriseUser:"+userid
        print(sql)
        value = r.delete(sql)
        print(value)
        return value