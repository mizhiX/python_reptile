import urllib.request
import urllib.parse
import time
import re

def main():
	start_page = int(input('请输入起始页码:'))
	end_page = int(input('请输入结束页码:'))
	url = 'http://www.yikexun.cn/lizhi/qianming/list_50_{}.html'
	# 打开文件
	fp = open('lizhi.html', 'w', encoding='utf8')
	for page in range(start_page, end_page + 1):
		# 构建请求对象
		request = handle_request(url, page)
		# 发送请求，得到响应
		content = urllib.request.urlopen(request).read().decode('utf8')
		# 解析内容
		parse_content(content, fp)
		time.sleep(2)
	fp.close()

def parse_content(content, fp):
	pattern = re.compile(r'<div class="art-t">.*?<a href="(.*?)">(<b>)?(.*?)(</b>)?</a>.*?</div>', re.S)
	ret = pattern.findall(content)

	# 遍历列表，取出标题和链接
	for tp in ret:
		href = 'http://www.yikexun.cn' + tp[0]
		title = tp[2]
		# 取出b标签
		# title = title.strip('</b>')
		text = get_text(href)
		# 打开文件，写入文件中
		string = '<h1>%s</h1>%s' % (title, text)
		fp.write(string)
		time.sleep(2)


def get_text(href):
	# 构建请求对象
	request = handle_request(href)
	content = urllib.request.urlopen(request).read().decode('utf8')
	pattern = re.compile(r'<div class="neirong">(.*?)</div>', re.S)
	ret = pattern.search(content)
	# print(ret.group(1))
	# exit()
	return ret.group(1)

def handle_request(url, page=None):
	if page:
		url = url.format(page)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
	}
	request = urllib.request.Request(url=url, headers=headers)
	return request

if __name__ == '__main__':
	main()