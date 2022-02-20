# _*_ coding: utf-8 _*_
# @Time : 2022-02-15 21:03
# @Author : kyle Li
# @Version：V 0.1
# @File : cilixiong_movie.py
# @desc :  爬取“磁力熊电影”

import requests
from bs4 import BeautifulSoup

# 目的url
url = "https://www.cilixiong.com/movie/index#d#.html"

# 要爬取的分页数量
page_number = 2

for idx in range(1, page_number + 1):
    # 第一页的url地址
    if idx == 1:
        temp_url = url.replace("#d#", "")
    # 第一页之外的url地址
    else:
        temp_url = url.replace("#d#", f"_{idx}")

    # 发起该分页的请求
    r = requests.get(temp_url)
    # 状态码如果不等于200，则抛出异常
    if r.status_code != 200:
        print(r.status_code)
        raise Exception()
    # 设置编码为utf-8，防止乱码
    r.encoding = 'utf-8'
    # 设置解析器
    soup = BeautifulSoup(r.text, "html.parser")
    # 根据上面所说的内容  设置具体解析内容  得到该分页下的所有电影内容
    movie_list = (
        soup.find("div", class_="masonry masonry-demos")
            .find("div")
            .find_all("div")
    )
    # 对该分页下的所有电影内容进行解析
    for movie in movie_list:
        a_tag = movie.find("a")
        # 这就是每个电影详情的链接
        link = a_tag.get("href")
        img_tag = a_tag.find("figure").find("img")
        # 电影名称
        name = img_tag.get("alt")
        # 电影封面图
        img_url = img_tag.get("src")

        # 对电影的详情信息发出请求
        r = requests.get(link)
        r.encoding = "utf-8"
        soup = BeautifulSoup(r.text, "html.parser")
        # 磁力链接
        cili_link = soup.find("div", class_="tabs-container").find("a").get("href")
        # 豆瓣得分
        score = soup.find("span", class_="tiny-title").find("span").get_text()

        print(f"电影名称：{name}   电影封面图：{img_url}   豆瓣得分：{score}   磁力链接：{cili_link}")

