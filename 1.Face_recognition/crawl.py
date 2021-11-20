# -*- coding: UTF-8 -*-
# @Project: Face_recognition 
# @File: crawl 
# @Author: rtmacha
# @Date: 2021/09/25 9:17

import requests
from bs4 import BeautifulSoup
import time
import re

des_url = r"https://www.eng.okayama-u.ac.jp/ec/staff/"


def get_soup(url):
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        "Cookie": "_ga=GA1.1.1419198435.1631435519; _ga_1CBCNG3QX7=GS1.1.1631440160.2.1.1631440809.0",  # cookie改成你自己的
        "Referer": "https://www.eng.okayama-u.ac.jp/ec/staff/"
    }
    html = ""
    try:
        response = requests.get(url, headers=headers)  # 请求访问网站
        html = response.text  # 获取网页源码
        print("[" + time.strftime('%Y-%m-%d %H:%M:%S') + "] [INFO]: 爬取成功")
    except requests.exceptions.RequestException as e:
        print("[" + time.strftime('%Y-%m-%d %H:%M:%S') + "] [WARNING]: ", e)
    return BeautifulSoup(html, 'lxml')  # 格式化网页，使用lxml解析器


def get_img(soup):
    table_list = soup.find_all("table")
    img_list = []
    for table in table_list:
        img_list.append([i.get('src') for i in table.find_all('img')])

    # 参考：https://segmentfault.com/a/1190000018903731
    img_url_list = sum(img_list, [])  # 降维打击

    for i in range(len(img_url_list)):
        # file_name = re.search(r"[^/\\&\?]+\.\w{3,4}(?=([\?&].*$|$))", img_url_list[i], re.M|re.I).group()  # 匹配文件名字
        file_type = re.search(r".\w{3,4}(?=([\?&].*$|$))", img_url_list[i], re.M|re.I).group()  # 匹配文件名字
        try:
            with open("./picture/" + str(i) + file_type, 'wb') as f:
                print("[" + time.strftime('%Y-%m-%d %H:%M:%S') + "] [INFO]: 正在保存第{}张图片".format(str(i+1)))
                f.write(requests.get(img_url_list[i]).content)
        except requests.exceptions.RequestException as e:
            print("[" + time.strftime('%Y-%m-%d %H:%M:%S') + "] [WARNING]: ", e)


soup = get_soup(des_url)
get_img(soup)


