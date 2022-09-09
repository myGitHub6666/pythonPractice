# 1.1 基本数据类型
# 1.1.1 逻辑推理练习（类型转换）
print(bool(None)) # False 表示一个空对象
print(bool(" ")) # 空格表示有数据，返回True
# 当对数字bool时候，0是False，其他都是True
# 对于字符串bool时候，空字符串“” 和没有值得字符串None都是返回False
# bool函数对于空的[],(),{}都是返回False,其他都是返回True
print(4.0 == 4)  # True
print('4.0' == 4)  # False
print(bool('1'))  # True
print(bool("0"))  # True
print(str(32))  # 把数字类型的32转化为字符串‘32’
print(int(1.32))  # 把1.62转化成int类型，结果是1
print(float(32))  # 32.0
print(float('3.21'))  # 3.21
print(int("343"))  # 把字符串‘343‘转化成数字343
# print(int('3.34'))  # 报错，float类型的字符串 无法转化成int
print(bool(-1))  # True
print(bool(""))  # False
print(bool(0)) # False
print('wrqq' > 'acd')  # Ture 字符串比较大小

print('ttt' == 'ttt ')  # 最后面的空格，False
print('ttt' < 'ttt ') # True
# 空的ascii码是0， 空格的ascii码是32
print('sd'*3)  # sdsdsd 字符串可以相乘,生成一个新的字符串
print('wer' + "2322")  # wer2322 字符串可以相加
print(ord('a'))
print(ord("z"))
print(ord('A'))
print(ord("Z"))
print(ord(' ')) # 空格是32
# 字符串的比较是按照字母所对应的ascii码大大小来比较，按位比较，第一位比较出来后后面的字母就不在比较
# ascii码的排序 ""<" "<A<Z<a<z
# 任何数字类型数据，int，float都可以转化成字符串形式
# int类型的字符串 可以转化为int型
# float类型的字符串，不能转化成float类型







