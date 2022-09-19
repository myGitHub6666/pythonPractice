list1 = [1,2,3,5,6,3,2]
list2 = [2,5,7,9]

# count = 0
# list3 =[]
# 先将list1,list2进行去重操作
# set1 = set(list1)
# lst = list(set1)
# set2 = set(list2)
# lst2 = list(set2)
# print(lst)
# for i in lst:
#     print(f'list1---{i}---{count}')
#     for ii in lst2:
#         print(f'list2---{ii}---{count}')
#         if i == ii:
#             list3.append(ii)
#     count +=1
# print(list3) #[2, 5]
# 哪些整数在lst1中，也在lst2中
set1 =set(list1)
set2 = set(list2)
print(set1.intersection(set2),type(set1.intersection(set2))) # 在set1中也在set2中的数据。相当于是求交集。

# 哪些整数既在lst1中，不在lst2中
print(set1.difference(set2))

# 两个列表一共有哪些整数 相当于求并集
print(set1.union(set2))

