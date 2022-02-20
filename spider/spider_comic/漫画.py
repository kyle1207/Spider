# _*_ coding: utf-8 _*_
# @Time : 2022-02-14 21:23
# @Author : kyle Li
# @Version：V 0.1
# @File : 漫画.py
# @desc :

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
from os import path as osp
import urllib
from selenium import webdriver


# browser = webdriver.Chrome(r"C:\Users\LDZ\AppData\Local\Google\Chrome\Application\chromedriver.exe")
#
# html_str = browser.get('http://baidu.com')
#
# print(browser.title)

# 一个简单的下载器
def download(url, save_path):
    try:
        with open(save_path, 'wb') as fp:
            fp.write(urllib.urlopen(url).read())
    except Exception as et:
        print(et)


if __name__ == "__main__":
    """
    # 驱动
    driver = r"C:\Users\LDZ\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    # 浏览器实例
    browser = webdriver.Chrome(driver)
    # 漫画首页
    index_page = "https://www.1kkk.com/manhua63250/"
    # 加载页面
    browser.get(index_page)
    
    # 解析章节元素节点
    chapter_ele_list = browser.find_element_by_css_selector('#detail-list-select-1  li  a')
    
    chapter_list = []
    for chapter_ele in chapter_ele_list:
        chapter_list.append((chapter_ele.text, chapter_ele.get_attribute('href')))
    
    print(chapter_list)
    """
    # 驱动
    driver = r"C:\Users\LDZ\AppData\Local\Google\Chrome\Application\chromedriver.exe"
    # 浏览器实例
    browser = webdriver.Chrome(driver)
    # 漫画首页
    chapter_url = "https://www.1kkk.com/ch1-1062763/"
    save_folder = "./download"

    if not osp.exists(save_folder):
        os.mkdir(save_folder)

    image_idx = 1

    browser.get(chapter_url)  # 加载第一个页面

    while True:
        # 根据前文的分析，找到图片的URI地址
        # #barChapter > img:nth-child(2)
        # #imgloading
        image_url = browser.find_element_by_css_selector('#imgloading').get_attribute('src')
        save_image_name = osp.join(save_folder, ('%05d' % image_idx) + '.' + osp.basename(image_url).split('.')[-1])
        download(image_url, save_image_name)  # 下载图片

        # 通过模拟点击加载下一页，注意如果是最后一页，会出现弹窗提示
        browser.find_element_by_css_selector('a.next').click()
        try:
            # 找寻弹窗，如果弹窗存在，说明这个章节下载完毕，这个大循环也就结束了
            browser.find_element_by_css_selector('#bgDiv')
            break
        except NoSuchElementException:
            # 没有结束弹窗，继续下载
            image_idx += 1
