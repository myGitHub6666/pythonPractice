# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 True，
# 如果有一个False就是False
from collections.abc import Iterable


def my_all(seq):
    # for i in seq:
    #     if isinstance(i,(int,float)):
    #         if i == 0:
    #             return False
    #     if isinstance(i,bool):
    #         if i is False:
    #             return False
    #     if isinstance(i,Iterable):
    #         if bool(i) is False:
    #             return False
    # return True
    for i in seq:
        # 如果是数字，除了0是False，如果是迭代器，【】（） 就是False。如果是字符串，''是False
        if not i:
            return False
    return True

print(my_all([1,2,3,[1,2]]))
print('________________')
print(bool([]))
print(bool(()))
print(bool(''))
print(bool(0))
print(bool(' '))
print(bool({}))
print(bool('-'))
print(bool(1))
# 1 就是True，无线循环
while 1 :
    print("*******")



