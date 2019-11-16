#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql


# 建立链接
connect = pymysql.connect(
    host='115.28.108.130',
    port=3306,
    user="test",
    password="abc123456",
    db='api_test',
    charset='utf8'
                         )
# 建立游标
# cur = connect.cursor()
cur = connect.cursor(pymysql.cursors.DictCursor)  # 字典游标
# 执行sql
cur.execute('select * from user where name="张三"') # 不返回查询结果
cur.execute('select * from user where name="李六"')

# print(cur.fetchone())  # 取完缓存取就没了
# print(cur.fetchall())  # 元祖

# 修改
cur.execute('insert into user(name, passwd) values ("王八", 9999999)')
connect.commit()
cur.execute('select * from user where name="王八" and passwd=9999999 and id=41')
print(cur.fetchall())