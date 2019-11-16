#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


def demoGet1():
    response = requests.get('http://httpbin.org/get')
    # 解析响应
    print(response.status_code)  # 状态码
    print(response.text)  # 相应数据（文本）
# ---------------------------------------------------


def demoGet2():
    reponse = requests.get('http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好')
    print(reponse.status_code)
    print(reponse.text)
# ---------------------------------------------------


def demoGet3():
    reponse = requests.get('http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好')
    return reponse.status_code,reponse.text
# ---------------------------------------------------


def demoGet4():
    url = 'http://www.tuling123.com/openapi/api'
    date1 = {'key': 'ec961279f453459b9248f0aeb6600bbe', 'info': '你好'}
    reponse = requests.get(url, params=date1)
    print(reponse.status_code, reponse.text)
# demoGet4()
# ----------------------------------------------------


def demoGet5():
    url = "http://115.28.108.130:5000/add/"
    date2 = {'a': 1, 'b': 101}
    reponse = requests.get(url, params=date2)
    print(reponse.status_code, reponse.text)


# demoGet5()
# ----------------------------------------------------


def demoPost1():  # 纯文本表单格式application/x-www-form-urlencoded
    url = 'http://115.28.108.130:5000/api/user/login/'
    date3 = {'name': '张三', 'password': '123456'}
    reponse = requests.post(url, data=date3)
    print(reponse.status_code, reponse.text)


# demoPost1()
# -----------------------------------------------------


def demoPost2():
    url = 'http://httpbin.org/post'
    date4 = {'name': 'Vic', 'age': 22, 'home': 'China'}
    reponse = requests.post(url, data=date4)
    print(reponse.status_code, reponse.text)


# demoPost2()
# -----------------------------------------------------


def demoPost3():  # json
    url = 'http://115.28.108.130:5000/api/user/reg/'
    json1 = {"name": "张三", "password": "123456"}
    reponse = requests.post(url, json=json1)
    print(reponse.text, reponse.status_code)
    print("________________________________________________")
    print(reponse.text)  # 响应数据的文本格式
    print("________________________________________________")
    print(reponse.json())  # 响应文本转化成字典,当只有响应数据为json格式时才能转为字典

  
# demoPost3()
# -----------------------------------------------------


def demoPost5():
    url = 'http://115.28.108.130:8080/gasStation/process'
    json2= {"dataSourceId": "d2FuZ2hhbw==", "methodId": "00A", "CardInfo": {"cardNumber": "789987"}}
    reponse = requests.post(url, json=json2)
    print(reponse.status_code, reponse.json())


# demoPost5()
# -----------------------------------------------------
def demoXml1():
    url = 'http://httpbin.org/put'
    xml1 = '''
    <xml>
        <msg>
        hello
        </msg>
    </xml>
    '''
    headers = {"content-type":"application/xml"}  # 使用原始格式raw发送应指定内容类型
    reponse = requests.put(url, data=xml1, headers=headers)  # 当data接收字符串数据会原样发送，接收字典会进行url编码
    print(reponse.status_code, reponse.text)


# demoXml1()
# ----------------------------------------------------
def demoPost3Raw():
    url = 'http://115.28.108.130:5000/api/user/reg/'
    jsonRaw = '''
    {"name": "张三", "password": "123456"}
    '''.encode('utf-8').decode('latin-1')
    header = {"content-type": "application/json;cjarset = UTF-8"}
    reponse = requests.post(url, data=jsonRaw, headers=header)
    print(reponse.status_code, reponse.text, reponse.json())


# demoPost3Raw()
# ----------------------------------------------------
def demoPost2Raw():
    url = 'http://httpbin.org/post'
    raw = '''
    {"name": "Vic", "age": 22, "home": "China"}
    '''
    header ={"content-type":"application/json"}
    reponse = requests.post(url, data=raw, headers=header)
    print(reponse.status_code, reponse.json())


# demoPost2Raw()
# ----------------------------------------------------
def post_file():
    """上传文件接口"""
    url ='http://115.28.108.130:5000/api/user/uploadImage/'
    files ={'file': open(r'/Users/wanghao/Desktop/timg.jpeg','rb')}
    res =requests.post(url, files=files)
    print(res.text)


# post_file()
# ----------------------------------------------------
def demo1():
    url = "https://www.baidu.com/"
    reponse = requests.get(url)
    print(reponse.status_code)
    print(reponse.text)
    print(reponse.content)
    print(reponse.encoding)
    print(reponse.cookies)
    print(reponse.headers)
    # print(reponse.json())
    print(reponse.cookies.get("BDORZ"))
    print(reponse.cookies.items())
    reponse.encoding='UTF-8'
    print(reponse.encoding)


