lst = [1,2,3]
lst1 = [4,5,6]
print(id(lst))
print(id(lst1))
print(id(lst+lst1))
# 用于在列表末尾一次性追加另一个序列中的多个值
lst.extend(lst1)
print(lst)
print(id(lst))