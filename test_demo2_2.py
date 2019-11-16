#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
def acquire_user_session():
    session = requests.session()  # 新建一个会话
    url = 'http://115.28.108.130:5000/api/user/login/'
    data1 = {'name': '张三', 'password': '123456'}
    reponse = session.post(url, data=data1)
    print(reponse.text, reponse.cookies)
    #  GET
    url2 = 'http://115.28.108.130:5000/api/user/getUserList/'
    reponse2 = session.get(url2)
    print(reponse.text)


# acquire_user_session()
def acquire_user_cookie():
    url = 'http://115.28.108.130:5000/api/user/login/'
    data1 = {'name': '张三', 'password': '123456'}
    reponse = requests.post(url, data=data1)
    print(reponse.text)
    print(reponse.cookies)

    url2 = 'http://115.28.108.130:5000/api/user/getUserList/'
    cookies = {"PYSESSID": "ebd72870-c18d-11e9-9973-00163e06e52c", "session": "eyJlYmQ3Mjg3MC1jMThkLTExZTktOT"
                                                                              "k3My0wMDE2M2UwNmU1MmMiOnRydWV9."
                                                                              "EDqWkg.2gRqTTUkVACaEeUAGk8ADm99X-A "}
    reponse2 = requests.get(url, cookies=cookies)
    print(reponse.text)
    print(reponse.status_code)


# acquire_user_cookie()


def baidu_ocr():
    url = 'https://aip.baidubce.com/oauth/2.0/token?'
    parame1 = {
        "grant_type": "client_credentials",
        "client_id": "kPoFYw85FXsnojsy5bB9hu6x",
        "client_secret": "l7SuGBkDQHkjiTPU3m6NaNddD6SCvDMC"
               }
    reponse = requests.get(url, params=parame1)
    one = reponse.json()
    token = reponse.json()["access_token"]
    url2 = f'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={token}'  # '%s' %token
    data2 = {'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999'
                    '_10000&sec=1566125977725&di=5d9f6de1808b8ca611fb6bc156bd3b'
                    '82&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%'
                    '2Fitem%2F201705%2F15%2F20170515065704_AZPCW.thumb.700_0.jpeg'}
    two = requests.post(url2, data=data2)
    print(two.text)


baidu_ocr()
def baidu_ocr2():
    url = 'https://aip.baidubce.com/oauth/2.0/token?'
    parame1 ={
        "grant_type": "client_credentials",
        "client_id": "kPoFYw85FXsnojsy5bB9hu6x",
        "client_secret": "l7SuGBkDQHkjiTPU3m6NaNddD6SCvDMC"
    }
    reponse1 =  requests.get(url, params=parame1)
    one = reponse1.json()
    url2 = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?'
    parame2 = {
        "access_token": one["access_token"]
    }
    data = {
        "url": "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1"
               "566125977725&di=5d9f6de1808b8ca611fb6bc156bd3b82&imgtype=0&src=http%"
               "3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201705%2F15%2F20170515065"
               "704_AZPCW.thumb.700_0.jpeg"
    }
    reponse2 = requests.post(url2, params=parame2, data=data)
    print(reponse2.text)



baidu_ocr2()
