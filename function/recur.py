# 递归函数

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))

'''
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出
'''
'''
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。


Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
'''

# 优化版本
def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

# print('fact(1000) =',fact(1000))

print('------------------------------')

# 利用递归函数移动汉诺塔:
# move（n,a,b,c)是一个定义的函数，其中n代表A杆上有几个盘，a变量代表你要从哪里开始移动的那个杆，c变量代表要移到哪里的那个杆，b变量就代表过渡的那个杆；
# 它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量

def move(n, a, b, c):
	if n == 1:
		print('Move', n, 'from', a, 'to', c)
	else:
		# print('进入111111')
		move(n-1, a, c, b)
		# print('进入222222')
		move(1, a, b, c)
		# print('进入333333')
		move(n-1, b, a, c)


move(3, 'A', 'B', 'C')
