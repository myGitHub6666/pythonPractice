# 内置函数可以获得可迭代对象的长度，
# 例如字符串，列表，元组，字典，集合。
# 实现一个类似功能的函数，获得数据的长度。
from collections.abc import Iterable


def my_len(obj):
    """
    获得obj对象的长度
    :param obj:
    :return:
    """
    # if isinstance(obj,(str,list,tuple)):
    #     a = 0
    #     for i in obj:
    #         a +=1
    #     return a
    #
    # if isinstance(obj,dict):
    #     a =0
    #     for key in obj.keys():
    #         a +=1
    #     return a
    # if isinstance(obj,set):
    #     a=0
    #     for i in set:
    #         a+=1
    #     return a
    # 这些对象都是迭代器，可以判断obj是不是可迭代的对象来判断
    # 先判断一下是否是迭代器对象，如果不是直接返回None
    if not isinstance(obj, Iterable):
        return None
    # 初始长度为0
    length = 0
    for i in obj:
        length += 1
    return length


if __name__ == '__main__':
    print(my_len(89))
