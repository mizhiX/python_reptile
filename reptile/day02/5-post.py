import urllib.request
import urllib.parse

# 加密的接口，如果想要得到，需要破解
url = 'http://fanyi.baidu.com/v2transapi'

word = 'wolf'
# 表单数据
formdata = {
	'from': 'en',
	'to': 'zh',
	'query': word,
	'transtype': 'realtime',
	'simple_means_flag': '3',
	'sign': '275695.55262',
	'token': '268ca3a468d99f5aac3a179efad0ab28',
}
# 处理表单数据
formdata = urllib.parse.urlencode(formdata).encode('utf8')
headers = {
	# 'Accept': '*/*',
	# 将其注释掉，索要完整的格式
	# 'Accept-Encoding': 'gzip, deflate',
	# 'Accept-Language': 'zh-CN,zh;q=0.9',
	# 'Connection': 'keep-alive',
	# 将其注释掉，让其自动计算即可
	# 'Content-Length': '120',
	# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie': 'BAIDUID=55279ECD6DDA84C66A41BA7CC1E6840E:FG=1; PSTM=1533627007; BIDUPSID=6F6C332F8A0E3C9949BD5D9F884F1FFB; PSINO=3; BDRCVFR[Y1-7gJ950Fn]=jCHWiyEa0lYpAN8n1msQhPEUf; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1465_26963_26432_21099_26350_26925_22157; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1533694190; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1533694190; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
	'Host': 'fanyi.baidu.com',
	'Origin': 'http://fanyi.baidu.com',
	'Referer': 'http://fanyi.baidu.com/?aldtype=16047',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, data=formdata)

print(response.read().decode('utf-8'))