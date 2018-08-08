##day02爬虫

1.urllib.parse

​	处理参数或者url的

https%3A//www.baidu.com/s%3Fword%3D%E8%B5%B5%E4%B8%BD%E9%A2%96

​	urllib.parse.quote()

​		字母、数字、下划线、冒号、//、?、=等

​		如果有其他字符, 需要进行编码

​	urllib.parse.unquote()

​		注: 编码的时候只需要编码参数即可

​	urllib.parse.urlencode()

​		data是一个字典, 直接将字典的键和值转化我query_string格式, 并且实现url编码

2.构建参数或者url的

​	request = urllib.request.Request(url=url, headers=headers)

3.模拟各种请求方式

​	get

​		百度搜索

​	post

​		百度翻译

​		urlopen(url,data=None)

​		如果有data, 代表是post请求, 如果没有data, 代表是get请求, get的参数需要拼接url的后面

​		表单数据的处理

```python
		formdata = urllib.parse.urlencode(formdata).encodee('utf8')	
```

​	ajax-get

​		豆瓣电影排行榜

```python
https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=40&limit=20

  每页显示10条 数据
  第一页: start=0	limit=10
  第二页: start=10	limit=10
  第三页: start=20	limit=10
  第n页:	start=(n-1)*10	limit=10
```

​	ajax-post

​		肯德基店铺位置

4.URLError \ HTTPError

```python
	是异常处理类, 属于urllib.error这个模块

	URLError: 断网或者主机不存在的时候会触发
    Exception: 官方的异常基类, 所有的异常类都直接或间接的继承它
    HTTPError: 是URLError的子类, 如果多个except同事捕获, 注意将子类写到上面, 将父类写到下面
```

5.复杂get

```python
百度贴吧
	第一页：https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=0
	第二页：https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=50
	第三页：https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=100
	第n页：pn = (n-1) * 50
    
    需求: 输入贴吧名字, 输入要爬去的其实页码, 结束页码,  以贴吧的名字创建一个文件夹, 将每一页的内容全部拿下来保存到第n页.html文件中
```

6.Handler处理器、自定义Opener

```python
urlopen()
请求对象
为了解决代理和 cookie这些更加高级的功能而引入的
实现最简单的功能, 高级功能的步骤和这个步骤一模一样
```



7.代理

```python
生活中代理: 代练, 代价, 代购
程序中: 见代理小弟图↓
代理服务器: 快代理, 西祠代理, 芝麻代理, 阿布云代理
  ①浏览器中设置代理
  ②代码中设置代理
```

![代理小弟图](I:\python_reptile\代理小弟图.png)