# -*- coding:utf-8 -*-

import pandas
import time
import random
import re
import json
import requests
from pyquery import PyQuery

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}
data = {
    "title": list(),
    "price": list(),
    "shop": list(),
    "comment number": list()
}


def gain_msg(url: str):
    """
    
    :param url:
    :return:
    """
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    content = PyQuery(r.text)("#J_goodsList")("ul")("li")
    for d in content.items():
        title = d(".p-name.p-name-type-2")("em").text()
        price = d(".p-price")("i").text()
        shop = d(".p-shop")("a").text()
        comment_num = comment_count(d.attr("data-sku"))
        data["title"].append(title)
        data["shop"].append(shop)
        data["price"].append(price)
        data["comment number"].append(comment_num)


def comment_count(product_id: str):
    """
    根据商品id获取评论数
    :param product_id:
    :return:
    """
    time.sleep(random.randint(4, 10) / 10)
    url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + str(
        product_id) + "&callback=jQuery9202324&_=1618887754397"
    res = requests.get(url, headers=headers)
    res.encoding = 'gbk'
    text = re.findall("jQuery9202324\((.*)\)", res.text, re.S)[0]
    text = json.loads(text)
    comment_count = text['CommentsCount'][0]['CommentCountStr']
    '''对 + 进行操作'''
    comment_count = comment_count.replace("+", "")
    '''对 万 进行操作'''
    if "万" in comment_count:
        comment_count = comment_count.replace("万", "")
        comment_count = str(int(comment_count) * 10000)
    return comment_count


def get_page():
    """

    :return:
    """
    num = 6
    page = 1
    s = 1
    for i in range(1, num):
        if i == 1:
            url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&page=" + str(
                1) + "&s=" + str(1) + "+&click=0"
        else:
            url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&page=" + str(
                page) + "&s=" + str(s) + "+&click=0"
        print("page=" + str(page) + ",s=" + str(s))
        gain_msg(url)
        page = page + 2
        s = s + 60
        if i == 1:
            s = 56


if __name__ == '__main__':
    """"""
    # url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&pvid=773ce82cfdd641bfa60d65dc9845bc0b"
    # gain_msg(url)
    get_page()
    '''csv'''
    print(data)
    pandas.DataFrame(data).to_csv("../resource/jd/jd_data.csv", encoding="utf-8")
    '''json'''
    with open("../resource/jd/jd_data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False))
