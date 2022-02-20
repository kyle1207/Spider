# _*_ coding: utf-8 _*_
# @Time : 2022-02-10 21:42
# @Author : kyle Li
# @Version：V 0.1
# @File : test_urllib.py
# @desc :


import urllib.request

# get
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行utf-8解码

# post
import urllib.parse  # 解析器

data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))

