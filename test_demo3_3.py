#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import pymysql


def test_add_new_card():
    #  数据库连接
    connect = pymysql.connect(
        host='115.28.108.130',
        port=3306,
        user="test",
        password="abc123456",
        db='longtengserver',
        charset='utf8'
                          )
    #  SQL查询卡号是否已经被添加
    cur = connect.cursor(pymysql.cursors.DictCursor)
    cur.execute('select * from cardinfo where cardNumber = 1237890789')
    ret = cur.fetchall()
    card_value = ret[0]["cardNumber"]
    print(card_value)

    #  判断若卡号已经添加则删除
    if card_value == ret[0]["cardNumber"]:
        cur.execute('delete from cardinfo where cardNumber = 1237890789')
        connect.commit()
    else:
        pass

    #  已经删除存在卡，绑定该卡为新卡
    url = 'http://115.28.108.130:8080/gasStation/process'
    json = {
        "dataSourceId": "d2FuZ2hhbw==",
        "methodId": "00A",
        "CardInfo": {
            "cardNumber": "1237890789"
        }
    }
    reponse = requests.post(url, json=json)
    print(reponse.json())
    assert "添加卡成功" == reponse.json()['msg']
    cur.execute('select * from cardinfo where cardNumber = 1237890789')
    print(cur.fetchall())


test_add_new_card()

