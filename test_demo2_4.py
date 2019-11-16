#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

url = 'http://115.28.108.130:8080/gasStation/process'


def test_add__new_fuel_card():  # 添加加油卡
    json = {
        "dataSourceId":
            "d2FuZ2hhbw==",
        "methodId": "00A",
        "CardInfo":
            {
                "cardNumber": "1237890789"
            }
    }
    reponse = requests.post(url, json=json)
    print(reponse.json())
    # assert "添加卡成功" == reponse.json()["msg"]


test_add__new_fuel_card()

# 绑定加油卡


def test_banding_card():
    json = {
        "dataSourceId": "d2FuZ2hhbw==",
        "methodId": "01A",
        "CardUser":
            {
                "userName": "wanghao",
                "idType": "1",
                "idNumber": "wanghao119"
            },
        "CardInfo":
            {
                "cardNumber": "1237890789"
            }
    }
    reponse2 = requests.post(url, json=json)
    print(reponse2.json())
    # assert "每个用户只能绑定两张卡" == reponse2.json()["msg"], 5014 == reponse2.json()["code"]


test_banding_card()

# 消费加油卡接口


def test_expenditure_card():
    json = {
        "dataSourceId": "d2FuZ2hhbw==",
        "methodId": "04A",
        "CardUser":
            {
                "userId":357753
            },
        "CardInfo":
            {
                "cardNumber": "123789000000",
                "cardBalance": "50"
            }
    }
    reponse3 = requests.post(url, json=json)
    print(reponse3.json())
    assert 200 == reponse3.json()["code"], "消费成功!" == reponse3.json()["mag"]


# test_expenditure_card()

# 充值加油卡
def test_topup_card():
    json = {
        "dataSourceId": "d2FuZ2hhbw==",
        "methodId": "03A",
        "CardInfo":
            {
                "cardNumber": "789987",
                "cardBalance": "50"
            }
    }
    reponse4 = requests.post(url, json=json)
    print(reponse4.json())
    assert '充值成功' == reponse4.json()['msg'], '789987' == reponse4.json()["result"]["cardNumber"]

# test_topup_card()


def test_refer_card():
    data = {
        "dataSourceId": "bHRz",
        "userId": "357753",
        "cardNumber": "123789000000",
        "methodId": "02A"
    }
    reponse5 = requests.get(url, params=data)
    print(reponse5.json())
    assert '成功返回' == reponse5.json()['msg'], '已经被绑定,正常使用中' == reponse5.json()['result']['cardStatus']


# test_refer_card()
# pytest *****.py
# pytest test_demo_4-2.py --html=test_report.html --self-contained-html





