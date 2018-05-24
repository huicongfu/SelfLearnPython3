'''
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果

通过remove(key)方法可以删除元素
'''

s1 = set([1,1,2,2,3,3])
print(s1)
s2 = set([2,3,4])

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
print(s1 & s2)
print(s1 | s2)

tl = (1,2,3)
tl2 = (1,[2,3])
s3 = set([tl,4,5])
print(s3)
s4 = {'a':tl2,'b':'2'}
print(s4)

'''
list、turple有序可重复，可变
set dict 无序不重复 key值不可变，不可赋值list
'''