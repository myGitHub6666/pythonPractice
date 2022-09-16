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




