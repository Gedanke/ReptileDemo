# -*- coding:utf-8 -*-

import json
import matplotlib.pyplot as plt
import requests

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}

code = 161725
size = 365
url = "https://danjuanapp.com/djapi/fund/nav/history/" + str(code) + "?page=1&size=" + str(size)


def gain_data():
    """

    :return:
    """
    res = requests.get(url, headers=headers)
    res.encoding = "utf-8"
    '''json'''
    with open("../resource/fund/fund_data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(res.json(), ensure_ascii=False))


def test_data():
    """

    :return:
    """

    def print_msg(d: dict):
        """

        :param d:
        :return:
        """
        print('date: ', d["date"], '\tnav: ', d["nav"], '\tpercentage: ', d["percentage"], '\tvalue: ', d["value"])

    '''json'''
    with open("../resource/fund/fund_data.json", "r") as f:
        data = json.load(f)["data"]["items"]
    l = len(data)
    now = data[l - 1]["date"].split("-")[1]
    for i in range(l - 1, -1, -1):
        d = data[i]
        m = d["date"].split("-")[1]
        if m == now:
            print_msg(d)
        else:
            print("------")
            now = m
            print_msg(d)


def deal_data():
    """

    :return:
    """
    '''json'''
    with open("../resource/fund/fund_data.json", "r") as f:
        data = json.load(f)["data"]["items"]
    new_data = dict()
    l = len(data)
    now = " "
    for i in range(l - 1, -1, -1):
        d = data[i]
        m = d["date"].split("-")[1]
        tmp = d["date"].split("-")
        month = tmp[0] + "-" + tmp[1]
        if m == now:
            new_data[month]["nav"].append(d["nav"])
            new_data[month]["percentage"].append(d["percentage"])
            new_data[month]["value"].append(d["value"])
        else:
            now = m
            new_data[month] = dict()
            new_data[month]["nav"] = list()
            new_data[month]["percentage"] = list()
            new_data[month]["value"] = list()
            new_data[month]["nav"].append(d["nav"])
            new_data[month]["percentage"].append(d["percentage"])
            new_data[month]["value"].append(d["value"])
    '''json'''
    with open("../resource/fund/data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(new_data, ensure_ascii=False))


def analysis_one():
    """

    :return:
    """
    '''json'''
    with open("../resource/fund/data.json", "r") as f:
        data = json.load(f)
    month = list()
    month_start = list()
    month_end = list()
    for key, value in data.items():
        month.append(key)
        l = len(value["value"])
        month_start.append(float(value["value"][0]))
        month_end.append(float(value["value"][l - 1]))
    ''''''
    bar_width = 0.25
    x = list(range(len(month)))
    xTicks = [i + bar_width for i in x]
    plt.figure(figsize=(20, 8), dpi=100)
    plt.bar(x, month_start, width=bar_width, label="Beginning of month")
    plt.bar(xTicks, month_end, width=bar_width, label="End of month")
    plt.xlabel("month")
    plt.ylabel("value")
    plt.xticks(xTicks, month)
    plt.legend()
    plt.savefig("resource/fund/a_1.png")
    plt.show()


def analysis_two():
    """

    :return:
    """
    '''json'''
    with open("../resource/fund/data.json", "r") as f:
        data = json.load(f)
    month = list()
    month_high = list()
    month_low = list()
    for key, value in data.items():
        month.append(key)
        month_high.append(float(max(value["value"])))
        month_low.append(-float(min(value["value"])))
    ''''''
    bar_width = 0.25
    x = list(range(len(month)))
    xTicks = [i + bar_width for i in x]
    plt.figure(figsize=(20, 8), dpi=100)
    plt.bar(x, month_high, width=bar_width, label="Highest of month")
    plt.bar(xTicks, month_low, width=bar_width, label="Lowest of month")
    plt.xlabel("month")
    plt.ylabel("value")
    plt.xticks(xTicks, month)
    plt.legend()
    plt.savefig("resource/fund/a_2.png")
    plt.show()


def analysis_three():
    """

    :return:
    """
    '''json'''
    with open("../resource/fund/data.json", "r") as f:
        data = json.load(f)
    month = list()
    month_value = list()
    for key, value in data.items():
        month.append(key)
        month_value.append(float(max(value["value"])) - float(min(value["value"])))
    ''''''
    plt.figure(figsize=(20, 8), dpi=100)
    plt.plot(month, month_value, label="diff")
    plt.xlabel("month")
    plt.ylabel("value")
    plt.legend()
    plt.savefig("resource/fund/a_3.png")
    plt.show()


def analysis_four():
    """

    :return:
    """
    '''json'''
    with open("../resource/fund/data.json", "r") as f:
        data = json.load(f)
    month = list()
    month_value = list()
    for key, value in data.items():
        month.append(key)
        l = len(value["value"])
        month_value.append(float(value["value"][l - 1]) - float(value["value"][0]))
    ''''''
    plt.figure(figsize=(20, 8), dpi=100)
    plt.plot(month, month_value, label="diff")
    plt.xlabel("month")
    plt.ylabel("value")
    plt.legend()
    plt.savefig("resource/fund/a_4.png")
    plt.show()


if __name__ == '__main__':
    """"""
    # gain_data()
    # test_data()
    # deal_data()
    # analysis_one()
    # analysis_two()
    # analysis_three()
    # analysis_four()
