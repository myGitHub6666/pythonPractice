dict1 = {'name':"lucy","age":18,'2':"编号"}
# 获取键的方法
for k in dict1:
    print(k,type(k))
for k in dict1.keys():
     print(k)
# 获取值得方法
for v in dict1.values():
    print(v,type(v))
# 对键值对进行遍历
for k,v in dict1.items():
    print(k,v)
list1 = []
for i in dict1:
    list1.append(i)
if '2' in list1:
    print('键中含有2')
else:
    print('2不在键中')
# 通过input输入3个人的信息，每个人有名字的年龄，将信息存入字典，并保存在列表里
# list2 = []
# for  i in range(3):
#     dict2 = {}
#     input_name = input('请输入姓名：')
#     input_age = input('请输入年龄：')
#     dict2['name'] = input_name
#     dict2['age'] = input_age
#     list2.append(dict2)
# print(list2)

my_list = [{'id':1,'money':10},{'id':2,'money':20},{'id':3,'money':30},{'id':4,'money':40}]
# 如果id为奇数，对money加20，如果id为偶数，对money加10
for dict1 in my_list:
    if dict1['id'] %2 ==1:
        dict1['money'] = dict1.get('money') +20
    else:
        dict1['money'] = dict1.get('money') + 10
print(my_list)

# 列表去重，新建一个列表，将旧列表的数据对新列表进行添加，如果新列表中已经存在则不管，如果不存在则添加list
list3 = [1,2,3,5,6,4,3,2,6,24,65,2,2]
new_list =[]
# for i in list3:
#     if i in new_list:
#         continue
#     else:
#         new_list.append(i)
# print(new_list)
for i in list3:
    if i not in new_list:
        new_list.append(i)
print(new_list)
# 利用set集合的特点
set1 = set(list3)
print(set1,type(set1))
list5 = list(set1)
print(list5)




