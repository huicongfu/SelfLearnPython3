# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数


def hello(greeting, *args):
	if (len(args) == 0):
		print('%s!' % greeting)
	else:
		print('%s, %s!' % (greeting, ', '.join(args)))


hello('Hi') # => greeting='Hi', args=()
hello('Hi','Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello',args=('Michael', 'Bob', 'Adam')

# *names 表示把names这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart','Lisa')