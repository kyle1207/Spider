# _*_ coding: utf-8 _*_
# @Time : 2022-02-21 20:41
# @Author : kyle Li
# @File : baidufanyi.py
# @desc :
# 案例2.抓取百度翻译数据
# 准备参数
import requests

kw = input("请输⼊你要翻译的英语单词:")
dic = {"kw": kw}
# 请注意百度翻译的sug这个url. 它是通过post⽅式进⾏提交的. 所以我们也要模拟post请求
resp = requests.post("https://fanyi.baidu.com/sug", data=dic)
# 返回值是json 那就可以直接解析成json
resp_json = resp.json()
print(resp_json)
# {'errno': 0, 'data': [{'k': 'Apple', 'v': 'n.苹果公司，原称苹果电脑公司'....
'''
{'errno': 0, 'data': [
    {'k': 'Apple', 'v': 'n. 苹果公司，原称苹果电脑公司'}, 
    {'k': 'apple', 'v': 'n. 苹果; 苹果公司; 苹果树'}, 
    {'k': 'APPLE', 'v': 'n. 苹果'}, 
    {'k': 'apples', 'v': 'n. 苹果，苹果树( apple的名词复数 ); [美国口语]棒球; [美国英语][保龄球]坏球; '}, 
    {'k': 'Apples', 'v': '[地名] [瑞士] 阿普勒'}]}

'''
print(resp_json['data'][0]['v'])  # 拿到返回字典中的内容
