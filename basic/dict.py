#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python内置了字典：dict的支持，dict全称dictionary，
在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
'''

'''
要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value  d.get('Thomas', -1)
返回None的时候Python的交互环境不显示结果
'''

'''
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法
'''

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除  d.pop('Bob')

d = {
	'Michael':95,
	'Bob':75,
	'Tracy':85
}

print('d[\'Michael\'] =',d['Michael'])
print('d[\'Bob\'] =',d['Bob'])
print('d[\'Tracy\'] =',d['Tracy'])
print('d.get(\'Thomas\', -1) =',d.get('Thomas', -1))


