from bs4 import BeautifulSoup

# 将文档生成对象
# lxml是一个解析器, 官方也自带了一个解析器  html.parser, 但是一般都是用lxml,  效率更高
soup = BeautifulSoup(open('soup_test.html', encoding='utf8'), 'lxml')

# 打印毒性可以打印为字符串, 重写一个方法叫做 __str__
# print(type(soup))

# 根据标签名查找
# ret  = soup.a
# print(ret)

# 获取属性
# print(ret.attrs['href'])
# print(ret['href'])

# 获取内容
# print(ret.string)
# print(ret.text)
# print(ret.get_text())

# ret = soup.div

# print(ret.string)
# print(ret.text.replace('\t', '').replace('\n', ''))
# print(ret.get_text())

# ret = soup.find('a', title='望岳')
# ret = soup.find('a', class_='shangyin')
# ret = soup.find('a', id='后庭花')
# print(ret.string)

import re


# ret = soup.find('a', class_=re.compile(r'^su'))
# print(ret)

# ret = soup.find_all('a')
# print(ret[3].string)

# ret = soup.find_all('a', class_='du')
# print(ret)

# ret = soup.find_all('a', class_=re.compile(r'^su'))
# print(ret)

# ret = soup.find_all('a', limit=2)
# print(ret)

# ret = soup.select('.song > li > a')
# ret = soup.select('.song a')

# ret = soup.select('a[title=xiang]')
# print(ret)

# ret = soup.select('a')
# print(ret)

odiv = soup.find('div', class_='song')
# print(odiv)
ret = odiv.select('a')

print(ret)