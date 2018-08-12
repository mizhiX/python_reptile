import re

string = '男生都喜欢17岁的女孩'

# ret = string.replace('20', '30')


# 里面的数字无论多少都改为30, 正则替换
# 将正则表达式匹配的内容替换为指定的内容
pattern = re.compile(r'\d+')
# 参数1: 要替换的内容
# 参数2: 在哪个字符串中查找
ret = pattern.sub('30', string)


# 将这回调函数传递进去, 该函数的要求是有一个参数, 有一个返回值
# 
def fn(obj):
	# print(obj)
	age = int(obj.group())
	age += 1
	return str(age)

ret = pattern.sub(fn, string)

print(ret)