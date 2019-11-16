#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


def test_demo_get1():
    response = requests.get('http://httpbin.org/get')
    print(response.json())
    assert "https://httpbin.org/get" == response.json()['url']


# test_demoGet1()

def test_topup_card():
    url = 'http://115.28.108.130:8080/gasStation/process'
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