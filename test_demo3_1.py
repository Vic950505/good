#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import requests


# a = '010-12345678'
# result = re.findall('\d{3,4}-\d{7,8}', a)
# if result:
#     print(result)
#
# b = 'daba4f5ag3a568a'
# result2 = re.findall('a\d+', b)
# if result2:
#     print(result2)
#
# c = 'c123c233c44d4'
# result3 = re.findall('\d{1,3}', c)
# if result3:
#     print(result3)


url = 'https://movie.douban.com/chart'

ret = requests.get(url)
a = ret.text
b = re.findall('<img\ssrc..(\w{4,5}\w{1,3}.*).\s.*width.*/>',  a)

# print(a)
print(b)

url = "http://39.104.14.232/ecshop/wwwroot/flow.php?step=checkout"



from jsonpath import jsonpath


res = requests.get('http://115.28.108.130:5000/api/bookstore2/')
# print(res.json())
# r = jsonpath(res.json(), '$.store.book[?(@.price>10)].author')
# print(res.text)