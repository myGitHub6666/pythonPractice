def my_sum(lst):
    """
    返回列表里所有数据的总和
    如果列表里有非数字类型的数据，忽略不管
    其他的数据要进行相加
    :param lst:
    :return:
    """
    # 先要判断一个如果不是列表类型，就直接返回
    if not isinstance(lst,list):
        return lst
    sum = 0
    for i in lst:
        if not isinstance(i, (int, float)):
            continue
        else:
            sum += i
    return sum


if __name__ == '__main__':
    print(my_sum(['a', 'fg','354',78989]))
    print(my_sum('kjhkl'))
