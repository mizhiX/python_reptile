import urllib.request

url = 'https://www.baidu.com/'

# 如何定制UA
# 在这个头部不仅可以定制UA

headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}

# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)

# 发送请求, 直接打开这个请求对象
requests = urllib.request.urlopen(request)