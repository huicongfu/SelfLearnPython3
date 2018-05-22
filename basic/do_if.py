#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:

age = int(input('Input your age: '))

if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')

height = 1.68
weight = 48
bmi = weight / (height * height)
print('bmi = %f' % bmi)

# 布尔值可以用and、or和not运算
if bmi <= 18.5:
	print('过轻')
elif bmi > 18.5 and bmi < 25:
	print('正常')
elif bmi >= 25 and bmi < 28:
	print('过重')
elif bmi >= 28 and bmi < 32:
	print('肥胖')
elif bmi >= 32:
	print('严重肥胖')