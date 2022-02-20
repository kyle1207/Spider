# Python爬取“cilixiong”网站

> 此module为爬取电影网站的相关流程

### 网站首页分析：

- **第一步：因需要获取网站电影每一页的HTML代码，所以我们分析分页的规律**

  - 第一页

  ![1644927915643](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644927915643.png)

  - 第二页

  ![1644928092156](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644928092156.png)

  > **规律**：
  >
  > https://www.cilixiong.com/movie/index.html       第一页
  >
  > https://www.cilixiong.com/movie/index_2.html   第二页
  >
  > https://www.cilixiong.com/movie/index_3.html    第三页
  >
  > https://www.cilixiong.com/movie/index_4.html    第四页
  >
  > **可以发现，除了第一页以外，都可以用https://www.cilixiong.com/movie/index_页数.html的方式得到，第一页是https://www.cilixiong.com/movie/index.html **

**第二步：获取单个电影的信息规律**

- **通过浏览器的“检查元素“功能查看页面的html代码，可以发现每页的电影信息都藏在以下区域内**

  ```html
  <div class = "masonry masonry-demos">
  ```

  ![1644928498927](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644928498927.png)

-  **电影的缩略图**

  ```html
  更进一步发现，所有电影的缩略图都在
  <div class=” masonry masonry-demos”>下的
  <div class=” masonry__container masonry--active”>内的若干个div区域中
  ```

-  **一个电影的缩略图**， 电影的详情页面就在这些div区域中的a标签里 ![1644929136264](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644929136264.png)

-  电影的详情页面就在这些div区域中的a标签里得到

  ![1644929489198](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644929489198.png)

- 查看电影详情页面

  ![1644929972362](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644929972362.png)

  > 第0个span标签是电影名称，第1个是豆瓣评分，第2个是上映日期...
  >
  > 而电影的下载地址则是在<div class=“tabs-container “ 里的a标签中

  ![1644930083866](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644930083866.png)

### 编码

```python

import requests
from bs4 import BeautifulSoup

# 目的url
url = "https://www.cilixiong.com/movie/index#d#.html"

# 要爬取的分页数量
pages_number = 2

for idx in range(1, pages_number + 1):
  # 如果爬取第一页，把删掉就行了
  if idx == 1:
    temp_url = url.replace("#d#", "")
  # 除了第一页以外的其它元素   用_页数来代替#d#
  else:
    temp_url = url.replace("#d#", f"_{idx}")
  # 发起该分页的请求
  r = requests.get(temp_url)
  # 状态码要是不等于200就抛出异常
  if r.status_code != 200:
    print(r.status_code)
    raise Exception()
  # 设置编码为utf-8 防止乱码
  r.encoding = "utf-8"
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

```

