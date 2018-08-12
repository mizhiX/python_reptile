##day04爬虫

1.正则替换		见1-tihuan.py文件

```python
可以替换为固定的字符串
	ret = pattern.sub('xxx', string)
也可以传递一个函数, 将函数的返回值替换匹配的内容
	ret = pattern.sub(fn. string)
```



2.bs4		见2-soup.py文件

```python
bs4是什么? 是一个python的第三方模块, 用来解析html数据, 其提供的api接口就非常的人性化

安装:
  	pip install bs4
    pip install lxml	这是一个解析器, 
有可能出现问题.
将pip源, 默认在国外, 切换为国内源, 豆瓣源, 阿里源等
如何切换?
(1) 指令切换,	-i 源地址		只针对这一次的命令安装生效
(2) 永久切换,	在指定地方写一个配置文件即可
	windows
  		① 在文件资源管理器上输入 %appdata%
    	② 手动创建一个pip文件夹
      	③ 新建一个文件pip.ini
        ④ 写入如下内容即可
        	[global]
          	timeout = 6000
            index-url = http://pypi.douban.com/simple
            trusted-host = pypi.douban.com
	linux
    	①cd ~
      	②mkdir ~/.pip
        ③vi ~/.pip/pip.conf
        ④编辑内容和Windows的内容一样
    语法学习
    	fron bs4 import BeautifulSoup
      	步骤: 通过BeautifulSoup这个类, 可以将你的html文档生成一个对象, 然后这个对象会有一些方法供你使用, 就可以得到你想要的节点内容, 或者节点属性
          
          可以将本地文件或者网络文件生成对象, 先从本地文件开始
          (1) 根据标签名进行查找
          		soup.a 只能得到第一个符合要求的标签
          (2) 获取属性
          		soup.a.attrs  返回一个字典, 里面包含所有的属性和值
            	soup.a.attrs['href']
              	soup.a['href']
          (3) 获取内容
          		obj.string
            	obj.text
              	obj.get_text()
               如果标签里面只有内容, 那么三个获取结果都一样
               如果标签里面还有标签, 那么第一个获取的是None, 后两个获取的是纯文本本内容
          (4) find方法
          	soup.find('a', title='xxx')
            soup.find('a', id='xxx')
            soup.find('a', class_='xxx')
            返回一个对象, 只能找到第一个符合要求的节点
            选看: soup.find('a', class_=re.compile(r'xxx'))
            可以写正则表达式, 一般用的不多
          (5) find_all方法
          	返回一个列表,列表里面都是对象, 能找到所有符合要求的节点
            soup.find_all('a', limit=2)	找到前两个符合要求的节点
            其他同(4)
          (6) select方法
          	根据选择器得到自己想要的节点
            返回的是列表, 就算返回的是一个,也是一个列表
            常用选择器:
              	标签选择器	a div
                类选择器	 .lala .dudu
                id选择器	  #lala #dudu
                后代选择器	
                	div .lala p a		: 后面的是前面的子节点就行
                  	div > p > a			: 后面的必须是前面的直接子节点才行
                群组选择器	div, #lala, .dudu
                属性选择器	input[name=xxx] div[class=xxx]
            也可以通过子对象查找内容, 得到当前子对象里面符合要求的标签
```



3.bs4实例

​	三国演义下载		见3-sanguo.py文件

​	滚滚长江东逝水,浪花淘尽英雄,是非成败转头空,青山依旧在,几度夕阳红

​	白发哟樵江渚上,惯看秋月春风,一壶浊酒喜相逢,古今多少事,都付笑谈中

​	www.shishumingju.com



​	智联招聘		见4-zhilian.py文件



4.xpath简介

```python
xml是什么?  被设计用来传输和存储数据, 和json同处于一个位置,  但是目前以json居多
xml和html的不同点:
  (1) xml用来传输数据, html用来显示数据
  (2) xml的标签没有被预定义, html的标签是 预定义好的
  (3) xml具有自我描述性
常用的路径表达式:
  /		:	从根节点开始查找
  //	:	从任意位置开始查找
  .		:	从当前节点开始查找
  ..	:	从父节点开始查找
  @		:	选取属性
    
路径表达式举例:
  bookstore/book	:	从bookstores下面找book节点, book必须是bookstores的直接节点
  bookstore//book	:	从bookstores下面找book节点, book可以使用直接节点也可以是孙子节点
  //book			:	从文档中任意位置找book节点
  //@lang			:	查找所有拥有lang属性的节点
  bookstore/book[1]	:	直接子节点第一个book, 下标从1开始
  bookstore/book[last()] : 直接子节点最后一个book
  bookstore//book[last()] : 所有book里面的最后一个
  bookstore/book[last() - 1]:倒数第二个book
  bookstore/book[position()<3]:去除前两个book
  //title[@lang]	:	所有拥有lang属性的title节点
  //title[@lang=eng]:	所有的lang属性值为eng的title节点
  bookstore/*		:	bookstore下面所有的直接子节点
  bookstore//*		: 	bookstore下面所有的子节点
  //title[@*]		:	所有有属性的title节点
  //book/title | //book/price : 找到所有book节点下面的直接子节点title和price
    
    
  xpath函数
  	contains		:	包含
    starts-with		:	以某某开头
    ends-with		:	以某某结尾(貌似不能用)
   
 我们学的xpath是用在了html中, 由于html和xml很想, 所以有一个第三方库就封装了使用xpath来解析html数据的借口
	安装:
    	pip install lxml
    使用的时候, 首先需要使用插件进行测试xpath, 然后再来到代码中进行编写
    xpath插件使用:
      (1) 属性筛选
      	//input[@id='kw']	找到属性id值为kw的input节点
      (2) 层级筛选
      	//div[@id='head']/div/div[@id='u1']/a[2]
```