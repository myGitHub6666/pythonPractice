# min函数返回序列中的最小值，
# 传入的参数可以是列表，也可以是元组，
# 实现下面的函数，实现同样的功能，
# 如果序列里有非数字类型的数据，可以忽略,
# 如果序列是空的，可以直接返回None
def my_min(seq):
    '''
    返回序列中的最小值
    1 进行类型检查，不是列表和元组，返回None
    2 如果序列是列表或者元组但是是空，也返回None
    3 遍历列表的数据，如果类型不是数字类型，就忽略
    :param seq:
    :return:
    '''
    if not isinstance(seq, (list, tuple)):
        return None
    # 判空操作
    # if seq == [] or seq == ():
    #     return None
    if len(seq)==0:
        return None
    min_number = seq[0]
    for i in seq:
        if isinstance(i, (int, float)):
            if i <= min_number:
                min_number = i
    return min_number


if __name__ == "__main__":
    lst = [1,'a',2,3]
    t =(1,2,3)
    print(my_min(lst))