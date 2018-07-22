# 关键字参数
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
'''
def print_scores(**kw):
	print('    Name  Score')
	print('-----------------')
	for name, score in kw.items():
		print('%10s   %d' % (name, score))
	print()


print_scores(Adam=99, Lisa=88, Bart=77)

data = {
	'Adam Lee' : 99,
	'Lisa S' : 88,
	'F.Bart' : 77
}

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
print_scores(**data)


# 命名关键字参数

'''
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

def person(name, age, *, city, job):
    print(name, age, city, job)

和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

def person(name, age, *args, city, job):
    print(name, age, args, city, job)


使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

'''

def print_info(name, *, gender, city='Beijing', age):
	print('Personal Info')
	print('--------------')
	print('    Name: %s' % name)
	print('    Gender: %s' % gender)
	print('    City: %s' % city)
	print('    Age: %s' % age)
	print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai',age=18)



''' 
总结：

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

'''


