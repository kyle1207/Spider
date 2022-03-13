# Scrapy

## 01. 爬虫介绍

#### 1. 什么是爬虫？

> **网络爬虫**也叫**网络蜘蛛**，如果把网络比喻成一个蜘蛛网，那么蜘蛛🕷就是在网上爬来爬去的蜘蛛，爬虫程序通过请求url地址，根据响应的内容进行解析采集数据，
>
> e.g. 
>
> - 如果响应内容为html，分析dom结构，进行dom解析，或者re匹配
> - 如果响应内容是xml/json数据，就可以转**数据对象**，然后对数据进行解析

---

#### 2. 有什么作用？ 

通过有效的爬虫手段批量采集数据，可以降低人工成本，提高有效数据量，给予运营/销售的数据支撑，加快产品发展。 

![image](https://note.youdao.com/yws/api/personal/file/734769369243449783AC0567A0239F3F?method=download&shareKey=2965ef70a4ffeacd7d29b0a3f3b76cd0)
---

#### 3. 业界的情况

目前互联网产品竞争激烈，业界大部分都会使用爬虫技术对竞品产品的数据进行挖掘、采集、大数据分析，这是必备手段，并且很多公司都设立了`爬虫工程师`的岗位

---

#### 4. 合法性   

爬虫是利用程序进行批量爬取网页上的公开信息，也就是前端显示的数据信息。因为信息是完全公开的，所以是合法的。其实就像浏览器一样，浏览器解析响应内容并渲染为页面，而爬虫解析响应内容采集想要的数据进行存储。

---

#### 5. 反爬虫

爬虫很难完全的制止，道高一尺魔高一丈，这是一场没有硝烟的战争，码农VS码农   
反爬虫一些手段：

* **合法检测**：请求校验(useragent，referer，接口加签名，等)
* **小黑屋**：IP/用户限制请求频率，或者直接拦截
* **投毒**：反爬虫高境界可以不用拦截，拦截是一时的，投毒返回虚假数据，可以误导竞品决策
* ... ...

---

#### 6. 选择一门语言

爬虫可以用各种语言写, C++, Java都可以, 为什么要Python?

首先用C++搞网络开发的例子不多(可能是我见得太少)
然后由于Oracle收购了Sun, Java目前虽然在Android开发上很重要, 但是如果Google官方进展不顺利, 那么很有可能用Go语言替代掉Java来做Android开发. 在这计算机速度高速增长的年代里, 选语言都要看他爹的业绩, 真是稍不注意就落后于时代. 随着计算机速度的高速发展, 某种语言开发的软件运行的时间复杂度的常数系数已经不像以前那么重要, 我们可以越来越偏爱为程序员打造的而不是为计算机打造的语言. 比如Ruby这种传说中的纯种而又飘逸的的OOP语言, 或者Python这种稍严谨而流行库又非常多的语言, 都大大弱化了针对计算机运行速度而打造的特性, 强化了为程序员容易思考而打造的特性. 所以我选择Python

---

#### 7. 选择Python版本

有2和3两个版本, 3比较新, 听说改动大. 根据我在知乎上搜集的观点来看, 我还是倾向于使用”在趋势中将会越来越火”的版本, 而非”目前已经很稳定而且很成熟”的版本. 这是个人喜好, 而且预测不一定准确. 但是如果Python3无法像Python2那么火, 那么整个Python语言就不可避免的随着时间的推移越来越落后, 因此我想其实选哪个的最坏风险都一样, 但是最好回报却是Python3的大. 其实两者区别也可以说大也可以说不大, 最终都不是什么大问题. 我选择的是Python 3

---

#### 8. 爬虫基本套路

* 基本流程
  * 目标数据
  * 来源地址
  * 结构分析
  * 实现构思
  * 操刀编码
* 基本手段
  * 破解请求限制
    * 请求头设置，如：useragant为有效客户端
    * 控制请求频率(根据实际情景)
    * IP代理
    * 签名/加密参数从html/cookie/js分析
  * 破解登录授权
    * 请求带上用户cookie信息
  * 破解验证码
    * 简单的验证码可以使用识图读验证码第三方库
* 解析数据
  * HTML Dom解析
    * 正则匹配，通过的正则表达式来匹配想要爬取的数据，如：有些数据不是在html 标签里，而是在html的script 标签的js变量中
    * 使用第三方库解析html dom，比较喜欢类jquery的库
  * 数据字符串
    * 正则匹配(根据情景使用) 
    * 转 JSON/XML 对象进行解析

---

#### 9. python爬虫

* python写爬虫的优势
  * python语法易学，容易上手
  * 社区活跃，实现方案多可参考
  * 各种功能包丰富
  * 少量代码即可完成强大功能
* 涉及模块包
  * 请求
    * `urllib`
    * `requests`
  * 多线程
    * `threading`
  * 正则
    * `re`
  * json解析
    * `json`
  * html dom解析
    * `beautiful soup`
  * lxml
    * xpath
  * 操作浏览器
    * `selenium`

## 02. 工具的使用

#### 1. python爬虫

- python
- pycharm
- 浏览器
  - Chrome
  - Firefox
- fiddler

#### 2. fiddler使用
