# 将字符串 "abcd" 转成大写
print('abcd'.upper())
# 计算字符串 "cd" 在 字符串 "abcd"中出现的位置
print('dacb'.find('cd')) # 返回子字符串的起始位置索引，没有的话则返回-1
# 字符串 "a,b,c,d" ，请用逗号分割字符串，分割后的结果是什么类型的？
print("a,b,c,d".split(',')) # 分割后为数组
# "{name}喜欢{fruit}".format(name="李雷") 执行会出错，请修改代码让其正确执行
print("{name}喜欢{fruit}".format(name="李磊",fruit="苹果"))
string1= "Python is good"
# 请将字符串里的Python替换成 python,并输出替换后的结果
print(string1.replace('Python','python'))
# 有一个字符串 string = "python修炼第一期.html"，请写程序从这个字符串里获得.html前面的部分，要用尽可能多的方式来做这个事情
str = 'python修炼第一期.html'
print(str.split('.')[0])
print(str[0:str.find(".html")])
# 如何获取字符串的长度？
print(str)
print(len(str))
# "this is a book",请将字符串里的book替换成apple
print('this is a book'.replace('book',"apple"))
# "this is a book", 请用程序判断该字符串是否以this开头
str1 = "this a book"
print(str1.split(" ")[0] == "this")
print(str1.startswith('this'))
# "this is a book", 请用程序判断该字符串是否以apple结尾
print(str1.split(" ")[-1] == "apple")
print(str1.endswith("apple"))
# "This IS a book"， 请将字符串里的大写字符转成小写字符
print("This IS a book".lower())
# "This IS a book"， 请将字符串里的小写字符，转成大写字符
print("This IS a book".upper())
# " this is a book\n"， 字符串的末尾有一个回车符，请将其删除
print("this is a apple\n")
print(" this is a apple".lstrip())
print(' this is a apple\n'.strip())
str2 = "this is string example....wow!!!"
print(f">>>>>>>>:{str2[100:200]}") # 超出范围不会报错，只会返回空字符串
suffix = "is";
print(str2.endswith(suffix, 2, 4))
print(str2.endswith(suffix, 2, 6))
# 获取Python字符串中的某字符可以使用索引：
lang = 'python'
lang[0]
# p
lang[3]
# h
# 截取字符串中的一段字符串可以使用切片，切片在方括号中使用冒号:来分隔需要截取的首尾字符串的索引，方式是包括开头，不包括结尾
lang[1:4]
# yth
# 当尾索引没有给出时，默认截取到字符串的末尾
lang[1:]
# ython
# 当头索引没有给出的时候默认从字符串开头开始截取
lang[:3]
# pyt
# 当尾索引和头索引都没有给出的时候，默认返回整个字符串，不过这只是一个浅拷贝
lang[:]
# python
# 当尾索引大于总的字符串长度时，默认只截取到字符串末尾，很明显使用这种方法来截取一段到字符串末尾的子字符串是非常不明智的，应该是不给出尾索引才是最佳实践
# lang[3:100]
# hon
# 当头索引为负数时，则是指从字符串的尾部开始计数，最末尾的字符记为-1，以此类推，因此此时应该注意尾索引的值，尾索引同样可以为负数，如果尾索引的值指明的字符串位置小于或等于头索引，此时返回的就是空字符串
lang[-2:]
# on
lang[-2,2]
# ''
# 切片是Python中截取字符串最强大的功能。
# 以下列举部分Python字符串常用的方法：
# 使用len()方法获取字符串长度
len(lang)
# 6
# 使用in操作符判断某个子字符是否在字符串中
'p' in lang
# True
'ab' in lang
# False
# 使用max()和min()方法获取字符串中编码最值对应的字符
max(lang)
# y
min(lang)
# h
# 使用*操作符对字符串进行重复
lang * 2
# pythonpython
# 使用cmp()方法对两个字符串进行对比，比较方式是先比较两个字符串的第一个字符的ASCII值，相同则比较第二个，依次类推，如果相等则返回0，第一个更小则返回-1，第一个大则返回1
lang2 = 'qython'
lang3 = 'pythoa'
# cmp(lang, lang2)
# -1
# cmp(lang, lang3)
# 1
# cmp(lang, lang)
# 0
# 使用chr()方法将数值作为ASCII值转化为字符，类似于JavaScript中的String.fromCharCode()方法
chr(97)
# a
# 使用ord()方法获取字符的ASCII值，类似于JavaScript中字符串实例的charCodeAt()方法
ord('a')
# 97
# 使用str()方法将其他数据类型转化为字符串
num = 3.14
str(num)
# 3.14
# 将字符串的第一个字符大写
'python'.capitalize()
# Python
# 使用split()方法将字符串按照指定的字符串分隔，返回数组
'hello world'.split(' ')
# ['hello', 'world']
# 使用strip()、lstrip()、rstrip()方法分别去掉左右空格、左空格、右空格
' hello '.strip()
# hello
' hello '.lstrip()
# 'hello '
' hello '.rstrip()
# ' hello'
# 使用upper()、lower()方法对字符串中所有字符大写、小写
lang.upper()
# PYTHON
lang.lower()
# python
# 使用isupper()、islower()方法判断字符串中所有的字符是否都是大写、小写
'ABC'.isupper()
# True
'Abc'.islower()
# False
# 使用istitle()方法判断字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
'Hello World'.istitle()
# True
'I am A Boy'.istitle()
# False
# 使用swapcase()方法对字符串中所有的字符进行大小写互转，即小写变大写，大写变小写
'Abc'.swapcase()
# aBC
# 使用join()方法连接字符串数组
a = 'hello world'.split()
'-'.join(a)
# hello-world
# 使用find()方法判断一个字符串中是否含有某个子字符串，三个参数，第一个为必须，是指需要搜索的字符串，第二个和第三个参数则是指搜索的起始位置和终止位置，搜索得到则返回索引值，得不到则返回-1
'hello world'.find('llo')
# 2
'hello world'.find('lloe')
# -1
# 使用endswith()和startswith()方法判断一个字符串是否是以某个字符串结尾、开头，参数和find()一致
'hello'.startswith('he')
# True
'hello'.endswith('lle')
# False
# 反转字符串
a = lang[::-1]
# nohtyp
# 使用count()方法获取某个字符在字符串中出现的次数
lang = 'aaa111223'
lang.count('a')
# 使用index()方法获取某个字符在字符串中首次出现的位置的索引
lang.index('a')
# 0
lang.index('1')
# 3

