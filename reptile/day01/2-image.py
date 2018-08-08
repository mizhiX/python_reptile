import urllib.request

url = 'https://g.fp.ps.netease.com/doraemon/file/5b518098143cface38cfd7bbPPI1lK5U'

# 第一种方式，发送请求，获取响应
# response = urllib.request.urlopen(url)

# with open('meinv.jpg', 'wb') as fp:
# 	fp.write(response.read())

# 第二种方式，
urllib.request.urlretrieve(url, 'meinv2.png')