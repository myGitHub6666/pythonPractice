# 最后面的4应该书step
for i in range(3, 20,4): #3,7,11,15,19
    print(i)
range(10, -3, -4) # 10,6,2,-1
for i in range(10, 5,-1):# 空输出不了任何东西,
    print(i)
range(2, 12) # 2到11

print('*'*50)
# 利用range函数遍历列表
lst = [1, 3, 5, 2, 7, 9]
# len(lst)是列表的长度，也是元素的个数，但是使用range就取不到最后的值，因为是从0 开始取值
# 参照上面的代码，从后向前遍历
for i in range(len(lst)-1,-1,-1):
    print(lst[i])
print("-----------------")
# 遍历输出列表里的所有偶数
for i in lst:
    if i%2==0:
        print(i)
print("-----------------")
# 遍历列表，输出大于3的奇数
for i in range(len(lst)):
    print(lst[i])
print("-----------------")
for i in lst:
    if i%2 != 0 and i >3:
        print(i)
# 遍历字典
dic ={
    'python':90,
    'java':95
}
for key in dic:
    print(key,dic[key])
for key,value in dic.items():
    print(key,value)
# 从列表 lst = [1, 3, 5, 2, 7, 9, 10] 中寻找1个偶数并输出，
lst1 = [1, 3, 5, 2, 7, 9, 10]
for i in lst1:
    if i %2 == 0:
        print(i)
        break
print("-----------------")
# 寻找列表中的最大值,最小值 lst = [3, 6, 1, 8, 1, 9 , 2]
lst2 = [3, 6, 1, 8, 1, 9 , 2]
max_value = lst2[0]
for i in lst2:
    if max_value > i :
        continue
    else:
        max_value = i
print(max_value)
print("-----------------")
# 参照上面的代码，写代码寻找列表的最小值
min_value = lst2[0]
for i in lst2:
    if min_value > i:
        min_value = i
print(min_value)
print("-----------------")
# 写代码寻找列表里的最小偶数
list1 = []
for i in lst2:
    if i % 2 ==0:
        list1.append(i)
print(min(list1))
# 写代码寻找列表里的最大奇数
print("-----------------")
list2 = []
for i in lst2:
    if i % 2 != 0:
        list2.append(i)
print(list2)
max_jishu = list2[0]
for ii in list2:
    if max_jishu < ii:
        max_jishu = ii
print(max_jishu)
# 寻找组合
lst1 = [3, 6, 1, 8, 1, 9 , 2]
lst2 = [3, 1, 2, 6, 4, 8, 7]
for i in lst1:
    for ii in lst2:
        if i + ii ==10:
            print((i,ii))
print("-----------------")
# 参照上面的代码，寻找两个数的差的绝对值等于2的组合
for i in lst1:
    for ii in lst2:
        if abs(i-ii)==2: # abs()函数就是求两个数的绝对值的函数
            print((i,ii))
# 两个列表里各取出一个值，item1和item2， 请计算item1*item2的最大值
print("-----------------")
list3 =[]
for i in lst1:
    for ii in lst2:
        list3.append(i*ii)
print(max(list3))



