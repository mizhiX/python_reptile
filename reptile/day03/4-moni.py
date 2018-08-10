import urllib.request
import urllib.parse
import http.cookiejar

# 在代码中有没有一个东西和浏览器是一样的，能够保存cookie呢？下次发送的时候自动携带cookie

# 首先创建一个cookiejar对象, 要来保存cookiec
ck = http.cookiejar.CookieJar()
# 根据ck创建handler
handler = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(handler)

# 往下所有的请求, 都是opener.open()方法发送, 那么就会自动保存cookie和携带cookie

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018741029602'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}
request = urllib.request.Requset(url=post_url, headers=headers)
formdata = {
	'email': '你的账号',
	'password': '你的密码',
	'icode': '',
	'origURL': 'http://www.renren.com/home',
	'domain': 'renren.com',
	'key_id': '1',
	'captcha_type': 'web_login',
	'f': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVwDXbx3oN5RBHzVxzj2jwbsO3z8VmHcZ1HZQTdC3enq%26wd%3D%26eqid%3D834642bf0000b410000000055b6bac87',
}
formdata = urllib.request.urlencode(formdata).encode('utf8')
# 发送请求
r = opener.open(reqeust, data=formdata)
print(r.read().decode('utf8'))

get_url = 'http://www.renren.com/960481378/profile'

request = urllib.request.Requset(url=get_url, headers=headers)

r = opener.open(request)

with open('renren.html', 'wb') as fp:
	fp.write(r.read())