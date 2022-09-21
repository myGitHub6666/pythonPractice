# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中，下面是使用示例
lst = ['a', 'b', 'c']
for index, item in enumerate(lst):
    print(index, item)
    # 0 a
    # 1 b
    # 2 c
print('---------------------')


def my_enumerate(lst):
    '''
    1,可以将数据循环输出
    2，可以给数据前面加上索引编号
    :param lst:
    :return:
    '''
    # yield 和return 都会将数据返回给调用者，不同的是，return返回后函数就结束了
    # 而yield执行后，会保留当前的状态，等到下次循环的执行的时候，恢复之前的状态，继续执行
    for i in range(len(lst)):
        yield i, lst[i]


lst = ['a', 'b', 'd']
if __name__ == '__main__':
    for index, item in my_enumerate(lst):
        print(index, item)
