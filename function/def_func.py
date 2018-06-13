'''
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return
'''

# def my_abs(x):
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x

'''
如果想定义一个什么事也不做的空函数，可以用pass语句：

def nop():
    pass

pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
'''

import math

# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
	if not isinstance(x,(int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x



def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

n = my_abs(-20)
print(n)

x,y = move(100,100,60, math.pi / 6)
print(x,y)

# TypeError: bad operand type:
# my_abs('123')

def quadratic(a, b, c):
	if a == 0:
		raise TypeError('a 不能为0')
	if not isinstance(a, (int, float)):
		raise TypeError('Bad operand type')

	if not isinstance(b, (int, float)):
		raise TypeError('Bad operand type')

	if not isinstance(c, (int, float)):
		raise TypeError('Bad operand type')
	
	s = (b * b) - (4 * a * c);

	if s < 0:
		print('无解')
		return

	b1 = (-b + math.sqrt(s))
	b2 = (-b - math.sqrt(s))
	return b1,b2

x = quadratic(2,3,1)
print(x)


'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。

'''