#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
'''
from collections import Iterable, Iterator

def g():
	yield 1
	yield 2
	yield 3

print('Iterable ? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable ? \'abc\':', isinstance('abc', Iterable))
print('Iterable ? 123:', isinstance(123, Iterable))
print('Iterable ? g():', isinstance(g(), Iterable))

print('Iterator ? [1, 2, 3]:',isinstance([1, 2, 3], Iterator))
print('Iterator ? iter([1, 2, 3]):',isinstance(iter([1, 2, 3]), Iterator))
print('Iterator ? \'abc\':', isinstance('abc', Iterator))
print('Iterator ? 123:', isinstance(123, Iterator))
print('Iterator ? g():', isinstance(g(), Iterator))

#iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
	print(x)

print('for x in [1, 2, 3, 4, 5]:')
for x in iter([1, 2, 3, 4, 5]):
	print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:',d)
for k in d.keys():
	print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
	print('value:', v)

# iter both key and  value:
print('iter item:', d)
for k, v in d.items():
	print('item:', k, v)


# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
#iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\'])')
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

#iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)

print('----------------------------------------------')

def findMinAndMax(L):
	if len(L) <= 0:
		return (None, None)
	min = max = L[0]
	print('min = %d,max = %d' % (min, max))
	for i, value in enumerate(L):
		print(i, value)
		if min > value:
			min = value;
		if max < value:
			max = value;
	return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')

