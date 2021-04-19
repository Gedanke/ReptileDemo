# -*- coding:utf-8 -*-

import requests
import json
import time

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}

u = "http://dgedanke.v4.dailiyun.com/query.txt?key=NP3AC4245B&word=&count=1&rand=false&ltime=0&norepeat=false&detail=false"
check_url = 'http://httpbin.org/ip'

if __name__ == '__main__':
    """"""
