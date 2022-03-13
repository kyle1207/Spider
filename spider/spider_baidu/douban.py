# _*_ coding: utf-8 _*_
# @Time : 2022-02-21 20:41
# @Author : kyle Li
# @File : douban.py
# @desc :
import json

import requests

url = 'https://movie.douban.com/j/chart/top_list'

param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',  # 从库中的第⼏部电影去取
    'limit': '20',  # ⼀次取出的个数
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

response = requests.get(url=url, params=param, headers=headers)

list_data = response.json()

fp = open('./douban.json', 'w', encoding='utf-8')
json.dump(list_data, fp=fp, ensure_ascii=False)
print('over!!!')
