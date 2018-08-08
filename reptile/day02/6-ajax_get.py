import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&'

print('每页显示20条数据')
page = int(input('请输入页码:'))
# 根据page计算出page_limit和page_start
page_limit = 20
page_start = (page - 1) * 20
data = {
	'page_limit': page_limit,
	'page_start': page_start
}

url += urllib.parse.urlencode(data)

headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf8'))
