dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
# 字典的长度是多少
print(len(dic))
# 请修改'java' 这个key对应的value值为98
dic['java'] = 98
print(dic)
# 删除 c 这个key
del dic['c']
print(dic)
# 增加一个key-value对，key值为 php, value是90
dic['php']= 90
print(dic)
# 获取所有的key值，存储在列表里
list1 = []
for k in dic.keys():
    list1.append(k)
print(list1)
# 获取所有的value值，存储在列表里
list2 = []
for v in dic.values():
    list2.append(v)
print(list2)
# 判断 javascript 是否在字典中
if 'javascript' in dic.keys():
    print('True')
else:
    print('False')
# 获得字典里所有value 的和
print(sum(list2))
# 获取字典里最大的value
print(max(list2))
# 获取字典里最小的value
print(min(list2))
# 字典 dic1 = {'php': 97}， 将dic1的数据更新到dic中
print(dic)
dic1 = {'php':97 }
dic.update(dic1) # 更新数据，或者修改数据
print(dic)
print(dic.keys(),type(dic.keys())) # dict_keys(['python', 'java', 'php']) <class 'dict_keys'>
# 小明去超市买水果
info ={
    '苹果':32.8,
    '香蕉':22,
    '葡萄':15.5
}
# 小明去购买了苹果，草莓，香蕉一共花了89元。小刚购买了葡萄，橘子，樱桃元一共花了87元，根据姓名获取这个人购买的水果种类和总费用
info={
    '小明':{
        '水果':['苹果','草莓','香蕉'],
        '总价':89
    },
    '小刚':{
        '水果':['葡萄','橘子','樱桃'],
        '总价':87
    }
}