import urllib.parse

url = 'https://www.baidu.com/s?word=赵丽颖'

# quote

string = urllib.parse.quote(url)

print(string)

# unquote

string2 = urllib.parse.unquote(string)

print(string2)


# urlencode
# 自动将中文转码	

url = 'https://www.baidu.com/s?'
# 将get参数写到这里
data = {
	'ie': 'utf8',
	'wd': '赵丽颖'
}

query_string = urllib.parse.urlencode(data)
url += query_string
print(url)

'''
# 将data拼接到url的后面, 尊称完整的url
# 遍历这个字典拼接成指定格式
lt = []
for k, v in data.items():
	value = k + '=' + v
	lt.append(value)
# 将lt用&符号拼接起来
query_string = '&'.join(lt)

url += query_string
print(url)
'''

