# 1，字符串转化为列表
str1 = '12345' # 这里面的数字12345，每一个都是字符串类性。
for i in str1:
    print(i)
    print(type(i))
list2 = list(str1) # 使用list（）内置函数直接进行转化
print(list2) # ['1', '2', '3', '4', '5']，里面的每一数字都是字符串形式的
# 使用列表推导式进行转化
str2 = '12345'
list3=[i for i in str2]
# 上面的类似于以下的过程
list4 =[]
for i in str2:
    list4.append(i) # i的取值本身就是字符串类性
print(list4) # ['1', '2', '3', '4', '5']
# 将字符串形式的列表进行转化，转换成列表
str3 = '[1,2,3,4,5]'
list5 = str3[1:-1].split(',')
print(list5) # ['1', '2', '3', '4', '5']
# 2,字符串转化为元组
str4 = '12345'
tuple1 = tuple(str4)
print(tuple1)  # ('1', '2', '3', '4', '5')
# 3 列表转元组
list6 = [1,2,3,4,5]
tuple2 = tuple(list6)
print(tuple2)
# 4,列表转字符串
list7 = [1,2,3,4,5]
str5 = str(list7)
print(str5,type(str5))  # '[1,2,3,4,5]'只能转化为字符串形式的列表
# 如果需要将列表中的元素拼接成一个字符串输出，就需要jion方法实现
list8 = [str(i) for i in list7]
print(list8) # ['1', '2', '3', '4', '5']
str6 =''.join(list8)
print(str6,type(str6)) # '123456'  <class 'str'>
# 5,元组转字符串
tuple3 = (1,2,3,4,5)
str7 = str(tuple3)
print(str7) # '(1, 2, 3, 4, 5)'
# 使用join实现将元素打包成字符串
str8 = ''.join([str(i) for i in tuple3])
print(str8,type(str8)) # '12345' <class 'str'>
# 元组转化为列表
tuple4 = (1,2,3,4,5)
list9 = list(tuple4)
print(list9)
# 使用列表推导式进行转化
list10 = [i for i in tuple3]
print(list10) # [1, 2, 3, 4, 5]
