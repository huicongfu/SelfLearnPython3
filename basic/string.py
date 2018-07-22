# 把Unicode编码转化为“可变长编码”的UTF-8编码
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# Python对bytes类型的数据用带b前缀的单引号或双引号表示  x = b'ABC'

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# 'ABC'.encode('ascii')   '中文'.encode('utf-8')

# 要把bytes变为str，就需要用decode()方法

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节

# 要计算str包含多少个字符，可以用len()函数，len()函数计算的是str的字符数

# 如果换成bytes，len()函数就计算字节数  len(b'ABC')

#!/usr/bin/env python3        第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# -*- coding: utf-8 -*-       第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

# %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略

# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
# 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)

print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

print('----------------------')

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('小明成绩提升了%2.1f%%' % r) #方法1
print('小明成绩提升了{0:.1f}%'.format(r)) #方法2