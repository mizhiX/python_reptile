import urllib.request
import urllib.parse

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
cname = input('请输入要查询的城市: ')
data = {
	'cname': cname,
	'pid': '',
	'pageIndex': '1',
	'pageSize': '10'
}
data = urllib.parse.urlencode(data).encode('utf-8')

headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request, data=data)

print(response.read().decode('utf8'))