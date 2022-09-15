lst = [1,2,3]
lst1 = [4,5,6]
print(id(lst))
print(id(lst1))
print(id(lst+lst1))
# 用于在列表末尾一次性追加另一个序列中的多个值
lst.extend(lst1)
print(lst)
print(id(lst))
num = 3.12
num1 = int(num)
print(num)
print(type(num1))
print(type(num))
print(float(3))
print(float('2.454'))
print(float('3435'))
name = "lucy"
age = 12
height = 1.46
num =1
stu_num = 90
print('我的名字是%s，我的年龄是%d，我的身高是%.1f，我的学号是%04d,考试的及格率为%d%%'%(name,age,height,num,stu_num))
print(f"我的名字是{name},年龄是{age},身高是{height:.3f},\n学号是{num:06d},及格率是{stu_num}%")
string1 = "kshfkdhf"
for i in string1:
    if i =="h":
        continue
    print(i)
print("*"*23)
for i in string1:
    if i != "f":
        print(i)
print(r'I\\\'m小明')
print(r'I\'m 小明')
print('I\'m 小明')
string2 = 'udhfjdk jkd jlk l  jkldjf kjlk '
print(string2.split())
print(string2.split(maxsplit=1))
string3 = ['a','b','c','a']
print(string3.count('a'))
if 'a' in string3:
    print('存在')
s1 = string3[::-1]
print(s1)
print(s1) # 产生一个新列表，原来的列表不会发生改变
string3.reverse()
print(string3) # 直接修改原来的列表
print(string3.index('a'))
str3 = ' and '.join(string3)
print(str3)
print(type(str3))
# 将字符串转化为list1存储
list1 = list('jhdfjkdhf')
print(list1)
# 合并列表，并没有产生新的列表，只是改变了列表的内容，地址没有改变
lst = [1,2,3]
print(id(lst))
lst2 = [4,5,6]
lst.extend(lst2) # 该操作没有返回值，返回None
print(lst.extend(lst2))
# 合并字符串，因为字符串是不可变的容器，所以重新生成了新的字符串，两次的id不一样
s1 = 'hdkjhfldkjfkl'
print(id(s1))
s2 = 'djhfkldjfk'
s1= s1+s2
print(s1)
print(id(s1))

