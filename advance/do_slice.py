#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# 倒数第一个元素的索引是-1。
'''
range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
方法：
range(stop)
range(start, stop[, step])   
# eg: range(0, 5, 1)

甚至什么都不写，只写[:]就可以原样复制一个list：
'''

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2] =', L[-2])
print('L[-2:-1] =',L[-2:-1])

R = list(range(100))
print('R[:10] =',R[:10])
print('R[-10:] =',R[-10:])
print('R[10:20] =',R[10:20])
print('R[:10:2] =',R[:10:2])
print('R[::5] =',R[::5])


print('R[-10] =',R[-10])


def trim(s):
	
	while s[:1] == ' ':
		s = s[1:]
	while s[-1:] == ' ':
		s = s[:-1]

	return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')