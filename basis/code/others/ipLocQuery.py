# -*- coding: utf-8 -*-


import IPy
import requests

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}


def getIpapiIP(ip):
    """

    :param ip:
    :return:
    """
    url = 'http://ip-api.com/json/'
    res = requests.get(url + ip, headers=headers)
    data = res.json()
    city = data.get('city')
    country = data.get('country')
    region_name = data.get('regionName')
    latitude = data.get('lat')
    longitude = data.get('lon')
    result = '-' * 50 + '\n' + \
             '''[ip-api.com 查询结果-IP]: %s\n经纬度: (%s, %s)\n国家: %s\n地区: %s\n城市: %s\n''' % (
                 ip, longitude, latitude, country, region_name, city) \
             + '-' * 50
    return result


def getIpstackIP(ip):
    """

    :param ip:
    :return:
    """
    url = 'http://api.ipstack.com/{}?access_key=1bdea4d0bf1c3bf35c4ba9456a357ce3'
    res = requests.get(url.format(ip), headers=headers)
    data = res.json()
    continent_name = data.get('continent_name')
    country_name = data.get('country_name')
    region_name = data.get('region_name')
    city = data.get('city')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    result = '-' * 50 + '\n' + \
             '''[ipstack.com 查询结果-IP]: %s\n经纬度: (%s, %s)\n板块: %s\n国家: %s\n地区: %s\n城市: %s\n''' % (
                 ip, longitude, latitude, continent_name, country_name, region_name, city) \
             + '-' * 50
    return result


def isIP(ip):
    """
    IP地址有效性验证
    :param ip:
    :return:
    """
    try:
        IPy.IP(ip)
        return True
    except:
        return False


def main(ip):
    """

    :param ip:
    :return:
    """
    separator = '*' * 30 + 'IPLocQuery' + '*' * 30
    if isIP(ip):
        print(separator)
        print(getIpstackIP(ip))
        print(getIpapiIP(ip))
        print('*' * len(separator))
    else:
        print(separator + '\n[Error]: %s --> 无效IP地址...\n' % ip + '*' * len(separator))


if __name__ == '__main__':
    """"""
    ip = "47.99.100.192"
    main(ip)
