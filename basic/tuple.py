#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# 要定义一个空的tuple，可以写成() t = ()
# 但是，要定义一个只有1个元素的tuple，如果你这么定义 t = (1), 定义的不是tuple，是1这个数
# 所以，只有1个元素的tuple定义时必须加一个逗号, t = (1,)

# cannot modify tuple:
classmates[0] = 'Adam'