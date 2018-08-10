import urllib.request

url = 'http://www.renren.com/960481378/profile'
headers = {
	'cookie': '所登录的cookie信息粘贴进来',
	'user-agent': 'mozilla/5.0 (windoWS NT 6.1; Win64; x64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/68.0.3440.75 safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

r = urllib.request.urlopen(request)

with open('renren.html', 'wb') as fp:
	fp.write(r.read())