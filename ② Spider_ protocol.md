# ② Spider_ protocol 

## 1. ROBOTS Protocol

> 通过**robots**协议可以知道网站的各页面，哪些可以抓取，哪些不可以抓取

eg:

 [https://www.taobao.com/robots.txt](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.taobao.com%2Frobots.txt)（通常是网站后面加/robots.txt即可以看到，就是一个文本文件） 

```html
User-agent:  Baiduspider    #用户代理，可以理解为浏览器的身份标识，通过这个字段可以告诉服务器是  							#什么样的程序在请求网站，Baiduspider即百度的搜索引擎
Allow:  /article            #表示允许爬的内容
Allow:  /oshtml
Allow:  /ershou
Allow: /$
Disallow:  /product/         #表示不允许该用户代理爬的内容
Disallow:  /
```



## 2. HTTP/HTTPS Protocol

> 为了拿到和浏览器一样的数据（浏览器数据也许不会一次完成渲染），就需要了解http和https

![1644648445565](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644648445565.png)

- HTTP：
  - 超文本传输协议，明文传输，默认端口号80
- HTTPS：
  - http+ssl（安全套接字），会对数据进行加密，默认端口443
-  **差异**：https更安全，但是性能更低（耗时更长） 

## 3. 浏览器发送http请求的过程

![1644648704373](C:\Users\LDZ\AppData\Roaming\Typora\typora-user-images\1644648704373.png)

>  ps：爬虫在爬取数据的时候，不会主动的请求css、图片、js等资源，就算自己爬取了js的内容，也只是字符串，而不会执行。
>
> 故，爬虫要根据当前url地址对应的**响应**为准，当前url地址的elements的内容和url的响应不一样，
>
> `特别要注意tbody，经常在elements中有而响应中无`

- 页面上的数据在哪里？
  - 当前url地址对应的相应中
  - 其他url地址对应的相应中，如ajax请求
  - js生成：1、部分数据在响应中，2、全部由js生成

## 4. url的格式

```shell
host:   服务器的ip地址或者是域名
port：  服务器的端口
path：  访问资源的路径
query-string：  参数，发送给http服务器的数据
anchor：        锚点（跳转到网页的制定锚点位置，anchor也有主播的意思）
```

例：[http://item.jd.com/11936238.html#product-detail](https://links.jianshu.com/go?to=http%3A%2F%2Fitem.jd.com%2F11936238.html%23product-detail)，就是一个带**锚点**的url，会自动跳转到商品详情，但是要注意，一个页面带锚点和不带锚点的响应是一样的（写爬虫的时候，就可以直接删掉锚点的部分）

## 5. http请求格式

![img](https:////upload-images.jianshu.io/upload_images/17476306-5f2bbdde75125a6b?imageMogr2/auto-orient/strip|imageView2/2/w/621/format/webp)



如，在访问百度时，查看request headers的source时，就可以看到如下内容

```python
GET http://www.baidu.com/ HTTP/1.1  
#请求方法：get
#url：http:xxxx.com/
#协议版本:http1.1 然后换行
Host: www.baidu.com
#请求头部：host；值：www.baidu.com；换行，以下类似
Proxy-Connection: keep-alive    
#keep-alive表示支持长链接。为什么要用长连接：不用频繁握手挥手，提高效率
Upgrade-Insecure-Requests: 1    #升级不安全的请求：把http请求转换为https的请求
DNT: 1  #Do not track
    
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)    Chrome/76.0.3809.100 Safari/537.36  #浏览器的标识。名字/版本号。如果有模拟手机版的请求，改user agent即可，不同的user agent访问相同的url，可能会得到不同的内容

Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3  #浏览器告诉服务器自己可以接受什么样的数据

Referer: http://baidu.com/
Accept-Encoding: gzip, deflate  #告诉服务器自己可以接受什么样的压缩方式
Accept-Language: en-US,en;q=0.9 #告诉服务器自己可以接受什么样语言的数据，q：权重，更愿意接受哪种语言

Cookie: BAIDUID=B8BE58B25611B7BBA38ECFE9CE75841F:FG=1;BIDUPSID=B8BE58B25611B7BBA38ECFE9CE75841F; PSTM=1565080210;BD_UPN=12314753;delPer=0;BD_HOME=0;H_PS_PSSID=26522_1453_21118_29523_29521_29098_29568_28830_29221_26350_22159;BD_CK_SAM=1;PSINO=7;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=218_0_3_0_0_7_1_1_13_76_2_0_0_0_0_0_0_1565599571%7C3%230_0_1565599571%7C1; rsv_jmp_slow=1565599826516; H_PS_645EC=2c80At1Is237xdMOfC3ju2q0qlWJ%2FFlbD5N50IQeTrCHyIEsZN6yQYBgLHI; B64_BOT=1   #cookie：保存用户的个人信息。ps：cookie和session的区别：cookie保存在浏览器本地，不安全，存储量有上限，session保存在服务器，更安全，往往没有上限。cookie又分为request cookie和reponse cookie，在浏览器中可以查看
```

除了以上字段，可能还有referer（推荐）字段，表示当前url是从哪个url过来的；x-request-with字段，表示是ajax异步请求。

以上字段中，主要是user agent（模拟浏览器），cookie（反反爬虫）

### 1. **常见的请求方式**

- get：除了post，基本都用get，更常用
- post：常用于提交表单的时候（安全），传输大文件的时候（美观）

### **2. 响应状态码（status code）**

- 200：成功
- 302/307：临时转移至新的url
- 404：not found
- 500：服务器内部错误

### **3. 字符串知识复习**

- str类型和bytes类型
  - bytes：二进制类型，互联网上数据都是以二进制的方式传输的
- str：unicode的呈现形式

ps：ascii码是一个字节，unicode编码通常是2个字节，utf-8是unicode的实现方式之一，是一变长的编码方式，可以是1、2、3个字节

```
编码和解码的方式必须一致，否则会乱码
```