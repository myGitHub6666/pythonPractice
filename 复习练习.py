my_list = [1,2,3]
my_list1 = my_list[::-1]
print(my_list)
print(my_list1)
my_list1[1]=22
print(my_list)
print(my_list1)

my_list2 = [1,2,3]
my_list3 = my_list2.copy()
print(my_list2)
print(my_list3)
my_list3[1] =22
print(my_list2)
print(my_list3)

my_list4 =[1,2,3]
my_list5 = my_list4
# 同一个列表，多了一个名字
print(id(my_list5))
print(id(my_list4))
my_list5[1] =22 # 要改变就一起改变
print(my_list4)
print(my_list5)

my_list5.sort()
print(my_list5)
print(my_list4)

my_list5.sort(reverse=True)
print(my_list5)
# 将列表转换为元组
tuple1 = tuple(my_list5)
# 将字符串转化为元组
string1 = 'hjdhfdjkjf'
tuple2 = tuple(string1)
print(tuple2)
print(tuple1)

# 将元组转化为列表
l1 = list(tuple1)
print(l1)
# 将字符串转化为列表
l2 = list(string1)
print(l2)

# 将元组转化为字符串
t = ('1','2','3')
tt =''.join(t)
# tt 是string类型
print(type(tt))
print()
# 将列表转化为字符串
t1 = ['s','d','d']
t2 = ''.join(t1)
print(str(t2))

dict1 = {'age':12,'name':'xiaozin','sex':'男'}
print(dict1['age'])
print(dict1.get('name'))
print(dict1.get('sex','保密'))
print(dict1)
for i in dict1:
    print(i)
for i in dict1.keys():
    print(i)
for value in dict1.values():
    print(value)
for k,v in dict1.items():
    print(k,v)
