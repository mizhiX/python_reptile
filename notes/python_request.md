# request模块的学习

## 安装

```python 
pip install request
```

## 发送get, post请求, 获取响应

```python 
response = request.get(url) # 发送get请求, 请求url地址对应的响应
response = request.post(url, data={请求体的字典}) # 发送post请求, 请求url地址对应的响应
```

## response的方法

```python
- response.text
	- 该方式往往会出现乱码, 出现乱码使用response.encoding='utf-8'
- response.content.decode()
	- 把响应的 二进制字节流 转换为 str 类型
  
- response.request.url	# 发送请求的url地址
- response.url	# response响应的url地址
- response.request.headers	# 请求头
- response.headers	# 响应请求
```

## 获取网页源码的正确打开方式

通过下面三种方式一定能获取到网页的正确解码之后的字符串

```python
1.  response.content.decode()	# 默认utf-8
2.  response.content.decode('gbk')	# 中文格式
3.  response.text	#推测
```

## 发送带header的请求

为了模拟浏览器, 获取和浏览器 一模一样的内容

```python
headers = {
    'User-Agend': 'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/61.0',
  'Referer':'https://www.hao123.com/'
}
response = request.get(url, headers=headers)
```

## 超时参数

```python
request.get(url, headers=headers, timeout=3) #3秒之内必须返回响应, 否则会报错
```

## retrying模块的学习

安装

```python
pip install retrying
```

```python
from retrying import retry

@retry(stop_max_attemot_number=3)	# 让被装饰的函数 反复执行三次, 三次全部报错才会报错, 中间有一次正常, 程序就会往后走
def fun1():
  print('this is func1')
  raise ValueError('this is test error') # 报错效果
```

## 处理cookie相关请求

```python
人人网{'email': 'mr_mao_hacker@163.com',
   'password': 'alarmchime'}
- 直接携带cookie请求 url地址
	1. cookie放在 headers中
  		headers = {
            'User-Agent': '...', 'Cookie': 'cookie字符串(自己的登录信息)'
        }
    2. cookie字典传给cookies参数
    	request.get(url, cookies=cookie_dict)
- 先发送post请求, 获取cookie, 带上cookie请求登录后的页面
	1. session = requests.session()	# session具有的方法和requests一样
  	2. session.post(url, data, headers)	# 服务器设置在在本地的cookie会保存在session
    3. session.get(url)	# 会带上之前保存在session中的cookie, 能够请求成功
```

## 数据提取方法

### json

数据交换格式, 看起来像python 类型(字典,列表)的字符串

```python
json.loads
	把json字符串转换为python类型
  使用json之前需要导入
  import json
  	json.loads(json字符串)
    
```



