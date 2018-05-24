# isExit = False
# num = ''
# while not isExit:
# 	if not isExit:
# 		print('请输入序号，1，2，3，')
# 		num = input('num :')
# 	if int(num) == 1:
# 		isExit = True
# 		continue


import math 

list1 = [12.34, 9.08, 73.1]

def area_sum(i):
	area = math.pi * i * i
	print(area)


for j in list1:
	area_sum(j)


