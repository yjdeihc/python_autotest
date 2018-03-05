# #coding=utf-8
import sys
import pymysql




def getconn(del_user_sql):
    # conn = pymysql.connect(host=host, user=user, passwd=passwd, port=port, db=db, charset=charset) #建立连接
    sql=del_user_sql
    print (sql)
    conn= pymysql.connect(host='erathinko.mysql.rds.aliyuncs.com',port = 3306,user='root',passwd='root',db ='root',charset="utf8")
    # cur = conn.cursor(cursor=pymysql.cursors.DictCursor)    #建立游标并指定游标类型
    cur = conn.cursor()
    cur.execute(sql)                      #执行sql
    if sql.startswith('select'):                #判断sql是否是select
      res = cur.fetchone()
    else:
      res = conn.commit()                      #insert\delete\update语句执行完毕后需要进行commit
    cur.close()                         #关闭游标
    conn.close()                        #关闭连接
    return res


def update_p(sql):
    print (sql)
    conn= pymysql.connect(host='erathinko.mysql.rds.aliyuncs.com',port = 3306,user='root',passwd='root',db ='root',charset="utf8")
    # cur = conn.cursor(cursor=pymysql.cursors.DictCursor)    #建立游标并指定游标类型
    cur = conn.cursor()
    cur.execute(sql)                      #执行sql
    res = conn.commit()                      #insert\delete\update语句执行完毕后需要进行commit
    cur.close()                         #关闭游标
    conn.close()                        #关闭连接
    return res

def get_id(sql):
    print (sql)
    conn= pymysql.connect(host='erathinko.mysql.rds.aliyuncs.com',port = 3306,user='root',passwd='root',db ='root',charset="utf8")
    # cur = conn.cursor(cursor=pymysql.cursors.DictCursor)    #建立游标并指定游标类型
    cur = conn.cursor()
    cur.execute(sql)                      #执行sql
    res = cur.fetchone()[0]
    #print(res)
    cur.close()                         #关闭游标
    conn.close()                        #关闭连接
    print(res)
    return res
