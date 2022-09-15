lst= [2,5,6,7,8,9,2,9,9]
# 找出列表里的最大值
print(max(lst))
# 找出列表里的最小值
print(min(lst))
# 找出列表里最大值的个数
print(lst.count(max(lst)))
# 计算列表里所有元素的和
print(sum(lst))
# 计算列表里元素的平均值
print(sum(lst)/float(len(lst)))
# 计算列表的长度
print(len(lst))
# 找出元素6在列表中的索引
print(lst.index(6))
print(lst[2])
# 在列表的末尾增加元素15
lst.append(15)
print(lst)
# 在列表的中间位置插入元素20
lst.insert(5,20)
print(lst)
# 将列表[2, 5, 6]合并到lst中
lst.extend([2,5,6])
print(lst)
# 移除列表中索引为3的元素
lst.pop(3)
lst.remove(lst[3])
print(lst)
# 翻转列表里的所有元素
lst1 = lst[::-1] #  反转得到新的列表
print(lst1)
lst.reverse()
print(lst) # 在原来列表的基础上用来反转
# 对列表里的元素进行排序，从小到大一次，从大到小一次
lst.sort()
print(lst)
lst.sort(reverse=True) # 从大到小排列
print(lst)