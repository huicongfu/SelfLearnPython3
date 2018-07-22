# 计算1+2+3+...+100:
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 100:
	acc = acc * n
	n = n + 1
print(acc)


# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

'''
要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。
大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句
'''
#break 语句
n = 1
while n <= 100:
	if n > 10: # 当n = 11时，条件满足，执行break语句
		break  # break语句会结束当前循环,跳出while
	print(n)
	n = n + 1
print('END')


#continue  跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0: # 如果n是偶数，执行continue语句
		continue   # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	print(n)


# 死循环
# n = 1
# while n > 0:
# 	n = n + 1
# 	print(n)