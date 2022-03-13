# _*_ coding: utf-8 _*_
# @Time : 2022-02-21 19:55
# @Author : kyle Li
# @File : baidu_html.py
# @desc :

'''
    第一种
'''
from urllib.request import urlopen

res = urlopen("http://www.baidu.com")
print(res.read().decode("utf-8"))

'''
    第二种
'''
import requests

kw = input("请输入你要搜索的内容：")
response = requests.get(f"https://www.sogou.com/web?query={kw}")
# print(response.text)
with open("sougou.html", mode="w", encoding="utf-8") as f:
    f.write(response.text)

