day01 - 爬虫1

1. 爬虫 概念

   爬虫是什么?

   ​	生活角度理解: 能够爬行的虫子 蜘蛛(spider)-->蜘蛛网

   互联网:	节点就是a链接(url) 统一资源定位符

   互联网爬虫:

   ​	写一个程序, 根据url去得到(抓取)指定的内容

   都有哪些语言可以实现爬虫:

   ​	① php. 号称世界上最好的语言, 爬虫做的不好, 天生对多进程和多线程支持的不好

   ​	② Java. 可以实现, 而且做的非常的号, 是python爬虫最主要的竞争对手, 做的不好, 语言不简洁, 代码臃肿, 重构成本非常高. 杀死一个程序员,只要修改三次需求

   ​	③C, C++. 也可以实现爬虫, 非常强大, 不好学, 编程语言排行榜前几名, 实现了,说明你厉害, 但是不是很好

   ​	④python. 可以实现爬虫, 号称世界上最优雅的语言, 代码简介, 学习成本低, 执行效率高, 非常强大的爬虫框架  (scrapy)

   通用爬虫

   ​	例子: 百度, 谷歌, 360, 搜狗, 必应等, 搜索引擎

   ​	做的工作: 

   ​		①从互联网上爬取所有的数据

   ​		②对数据存储并且处理

   ​		③给用户提供检索服务

   ​	如何让百度去抓取你的网站

   ​		①静静的等待, 百度会和DNS服务商合作

   ​		②主动提交自己的url: 百度开发者提交url

   ​		③在其他网站设置友情链接

   ​	如何让百度不抓取你的网站

   ​		君子协议, 口头协议: robots协议 

   ​		存放在网站的根目录下, 限制搜索引擎可以爬去哪些, 不可以爬取哪些

   ​		所以自己写的程序就不遵从了

   ​	网站排名 (SEO 网络优化)

   ​		①pagerank值排名, 根据点击量、浏览量等, 相当靠谱,口碑

   ​		②竞价排名: 魏泽西事件

   ​	通用爬虫缺点:

   ​		①抓取很多数据都是无效的	例: 百度搜索的除了第一页以外的页码1

   ​		②不能根据自己的需求抓取数据

   聚焦爬虫

   ​	根据自己特定的需求, 来抓取指定的数据

   ​	如何实现聚焦爬虫?

   ​	网页特点:

   ​		①网页都有自己唯一的url

   ​		②网页都是由html组成的

   ​		③网页传输都是使用http, https协议

   ​	思路:

   ​		①给一个url

   ​		②模拟浏览器发送http请求

   ​		③从html结构中提取指定的数据, 从字符串中根据规则提取指定的数据

   开发环境:

   ​	Windows系统, python3.x (64位) , sublime编辑器, PyCharm, vscode

   整体内容;

   ​	①涉及到python库

   ​		urllib, requests,selenium,jsonpath,lxml等一些库

   ​	②解析内容

   ​		正则表达式, bs4解析, xpath解析, jsonpath解析

   ​	③采集动态html

   ​		DOM操作, 动态的添加或者删除节点, selenium+phantomjs的到动态内容

   ​	④scrapy框架

   ​		异步高性能网络爬虫框架

   ​	⑤scrapy_redis分布式部署

   ​		在scrapy的基础上, 多了一套分布式部署的组件

   ​	⑥涉及到的爬虫-反爬虫-反反爬虫之间的斗争

   ​		反爬会伤害正式的用户, 一般情况下, 反爬也就这么两点: 第一个UA, 第二个封ip,第三个验证码, 光学识别, 打码平台

   ​		换思路解决问题, 其他网站, 手机端等

2. http协议

   协议是什么? 协议就是规定好的传输方式

   ###上网的原理

   一个网页要呈现爱面前, 一般需要15-30个请求

   不仅html是一个请求, css, js, 图片都要单独发送请求的

   ![说明](I:\爬虫\说明.png)

   http与https的区别

   http ://www.cnblogs.com/wqhwe/p/5407468.html

   ​	加密 : 公钥私钥

   ​	客户端: 123456用秘钥加密 ---> 服务器: 用秘钥解密得到123456

   ​		秘钥相同称之为对称加密

   ​		秘钥 不相同称之为非对称加密

   ​	客户端: 123456用公钥加密 ---> 服务器: 用私钥解密得到123456  反之相同

   http协议学历:

   ​	图解http协议:

   ​	http ://www.cnblogs.com/10158wsj/p/6762848.html

   ​	http协议是基于tcp的, 交互之前建立连接, 三次握手

   ​	udp传输协议, 只需要知道ip和端口即可发送消息

   ​	

   ​	请求: 包含请求行, 请求头, 请求内容

   ​		请求行: 请求方式, 请求资源, 协议版本号

   ​		请求头: 

   　　		HTTP请求中的常用消息头

   　　		accept:浏览器通过这个头告诉服务器，它所支持的数据类型
   　　		Accept-Charset: 浏览器通过这个头告诉服务器，它支持哪种字符集
   　　		Accept-Encoding：浏览器通过这个头告诉服务器，支持的压缩格式
   　　		Accept-Language：浏览器通过这个头告诉服务器，它的语言环境
   　　		Host：浏览器通过这个头告诉服务器，想访问哪台主机
   　　		If-Modified-Since: 浏览器通过这个头告诉服务器，缓存数据的时间
   　　		Referer：浏览器通过这个头告诉服务器，客户机是哪个页面来的  防盗链
   　　		Connection：浏览器通过这个头告诉服务器，请求完后是断开链接还是何持链接

   ​			X-Requested-With: XMLHttpRequest  代表ajax请求

   ​	响应: 响应行, 响应头, 响应内容

   ​		响应行里面, 常见的状态码

   ​		响应头, 对我们来说不重要

   	Location: 服务器通过这个头，来告诉浏览器跳到哪里
   	Server：服务器通过这个头，告诉浏览器服务器的型号
   	Content-Length: 服务器通过这个头，告诉浏览器回送数据的长度
   	Content-Language: 服务器通过这个头，告诉浏览器语言环境
   	Content-Type：服务器通过这个头，告诉浏览器回送数据的类型
   	Refresh：服务器通过这个头，告诉浏览器定时刷新
   	Content-Disposition: 服务器通过这个头，告诉浏览器以下载方式打数据
   	Transfer-Encoding：服务器通过这个头，告诉浏览器数据是以分块方式回送的
   	Expires: -1  控制浏览器不要缓存
   	Cache-Control: no-cache  
   	Pragma: no-cache
   ​		响应内容: html, css, js,  图片

   ​

3. 抓包工具

   ​	①谷歌浏览器自带抓包工具

   ​		右键开发者工具 --> network

   ​		XHR:XMLHttpRequest  前端要想发型ajax请求, 通过它创建对象, 发送请求

   ​		qurery_string_parameters : 请求字符串, get参数

   ​		formdata : 是post参数

   ​	②专业工具: fiddler

   ​		专业抓包工具, 比谷歌强在了跳转的时候很多请求都能抓取到

   ​		

4. urllib库

   ​	urllib库是什么?  自带的python库, 模拟发送http请求

   ​	python2系列: 分为urllib  urllib2

   ​	python3系列: urllib  --> 

   ​		urllib.request	模拟发送请求

   ​			urlopen(url) : 向url发送请求, 得到相应对象

   ​			urlretrieve(url, filepath) : 向url发送请求, 直接将响应写入到filepath中

   ​		response属性和方法

   ​			字符串格式 --> 字符格式

   ​				encode('utf-8)

   ​			字符格式 --> 字符串格式

   ​				decode('gbk)

   ​			response.read() : 读取字节格式内容

   ​			response.url  : 后去请求url

   ​			response.headers : 响应头部

   ​			response.status : 状态码

   ​		下载图片: 得到图片的src属性, 就可以将图片下载到本地

   ​		urllib.parse		处理参数或url

   ​		urllib.error		如何处理异常

   ​	

   ​