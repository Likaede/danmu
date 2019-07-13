# -*- coding: UTF-8 -*-
import requests
import random

# 下载弹幕
def GetDanmu(roomid):
    # 弹幕请求API
    url_get_danmu='https://api.live.bilibili.com/ajax/msg'
    # Post传递参数
    data={
        "roomid": roomid,
        "token": "",
        "csrf_token": "4029e662eeb468f43622725777ce06a3"
    }
    # 接受返回的信息
    response=requests.post(url_get_danmu,data=data)
    # print(response.json())
    # 转为字典
    list_danmu = response.json()
    # 提取弹幕内容
    # danmu=list_danmu['data']['room'][random.randint(5, 8)]['text']
    danmu = list_danmu['data']['room'][7]['text']
    # 这里要做成队列实时更新，要不然会重复弹幕
    print(danmu)
    return danmu

def Getroomid(num):
    url='https://api.live.bilibili.com/room/v1/Room/room_init?id='
    data={
        "id":num
    }
    response=requests.get(url,params=data)
    # print(response.json())
    roomid=response.json()['data']['room_id']
    print('实际房间号：'+ str(roomid))
    return roomid

if __name__ == '__main__':
    num=input('请输入直播间房间号：')
    roomid=Getroomid(num)
    while True:
        danmu=GetDanmu(roomid)