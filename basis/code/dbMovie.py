# -*- coding:utf-8 -*-


import operator
import time
import random
import json
import pandas
import requests

'''20'''
MOVIE_MAX_INDEX = 250
'''15'''
USER_MAX_INDEX = 4
headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Connection': 'keep-alive',
    "Host": "movie.douban.com"
}
movie_url = "https://movie.douban.com/subject/1291561/reviews?sort=hotest&start=5000"
user_url = "https://movie.douban.com/people/3302093/collect?start=0"


def gain_user_msg():
    """

    :return:
    """



if __name__ == '__main__':
    """"""
