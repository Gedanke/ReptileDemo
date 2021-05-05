# -*- coding:utf-8 -*-


import operator
import time
import random
import json
import pandas
import requests
import snownlp

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    "Host": "api.live.bilibili.com"
}
roomId = "8604981"
data = {
    'uid': list(),
    'nickname': list(),
    'timeline': list(),
    'text': list(),
    'isadmin': list()
}
data_list = [
    'uid', 'nickname', 'timeline', 'text', 'isadmin'
]
url = "https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid=8604981"
MAX = 10


def gain_data():
    """

    :return:
    """
    r = requests.post(url, headers=headers)
    '''key'''
    ''''text', 'uid', 'nickname', 'timeline', 'isadmin' '''
    admin = r.json()["data"]["admin"]
    room = r.json()["data"]["room"]
    for ad in admin:
        for dl in data_list:
            data[dl].append(ad[dl])
    for ro in room:
        for dl in data_list:
            data[dl].append(ro[dl])


def save_msg():
    """

    :return:
    """
    i = 0
    while True and i != MAX:
        time.sleep(random.randint(4, 6))
        gain_data()
        i += 1
    '''csv'''
    pandas.DataFrame(data).to_csv("../resource/bilibili/bilibili_data.csv", encoding="utf-8")
    '''json'''
    with open("../resource/bilibili/bilibili_data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False))


def analysis_data():
    """

    :return:
    """
    with open("../resource/bilibili/bilibili_data.json", "r") as f:
        d = json.load(f)
    d["text_analysis"] = list()
    count1, count2 = 0, 0
    for text in d["text"]:
        t = snownlp.SnowNLP(text)
        if t.sentiments > 0.5:
            d["text_analysis"].append(1)
            count1 += 1
        else:
            d["text_analysis"].append(-1)
            count2 += 1
    print("count1 : ", count1, "\t count2 : ", count2)
    '''analysis'''
    text = "".join(d["text"])
    s = snownlp.SnowNLP(text)
    dict_word = dict()
    s_word = s.words
    for it in s_word:
        dict_word[it] = s_word.count(it)
    dict_word = sorted(dict_word.items(), key=operator.itemgetter(1), reverse=True)[:10]
    for t in dict_word:
        print(t[0], "\t", t[1])


if __name__ == '__main__':
    """"""
    # save_msg()
    # print(data)
    # text1 = '不会真的有人喜欢这部电影吧'
    # s1 = snownlp.SnowNLP(text1)
    # print(text1, s1.sentiments)
    analysis_data()
