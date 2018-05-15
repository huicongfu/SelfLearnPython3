#以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。
#其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
#Python程序是大小写敏感的，如果写错了大小写，程序会报错。
a = 100
if a >= 0:
	print(a)
else:
	print(-a)


#Python能够直接处理的数据类型有以下几种：1，整数； 2，浮点数； 3，字符串

#字符串是以单引号'或双引号"括起来的任意文本
#如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容（注意：...不会在代码显示）

print("I'm ok")
print('I\'m \"ok\"')
print(r'\\\t\\') #输出：\\\t\\

print('''line1
line2
line3''')
print(r'''hello,\n world''')
