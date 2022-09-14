lst = [1, 2, 3, 4, 5]
# 求列表的长度
print(len(lst))


# 判断6 是否在列表中
if 6 in lst:
    print('True')
else:
    print(type(False))
    print(">>>>>>False")


def juge():
    for i in lst:
        if i == 6:
            print('True')
        else:
            print("False")


juge()
# lst + [6, 7, 8] 的结果是什么？[1,2,3,4,5,6,7]
lst1 = [6,7,8]
print(lst+lst1)
# lst*2 的结果是什么[1,2,3,4,5,1,2,3,4,5]
print(lst*2)
# 列表里元素的最大值是多少
print(max(lst))
# 列表里元素的最小值是多少
print(min(lst))
# 列表里所有元素的和是多少
print(sum(lst)) # 可以使用sum函数
def summ():
    sum = 0
    for i in lst:
        sum = sum + i
    print(sum)
summ()
# 在索引1的后面新增一个的元素10
lst.insert(1,10)# 直接在索引1的后面插入10即可
# lst[2]=10 给index=2的索引赋值10，是错误的
for i in lst:
    print(f"_______{i}")
# 在列表的末尾新增一个元素20
lst.append(20)# 默认追加在最后面
for i in lst:
    print(i)

# while True:
#     print("白嫖怪")