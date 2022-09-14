# 将列表中的所有数字修改成原来的两倍
# lst = [1, [4, 6.3], True]


# lst[0] = 2
# lst[1][0] =4
# lst[1][1] =12
def double_list(lst):
    for index, item in enumerate(lst):
        print(index, item)
        if isinstance(item, bool):
            continue
        if isinstance(item, (int, float)):  # 判断item是否是(int 或者float)元组中的一个类型，如果是则返回True
            lst[index] = lst[index] * 2
        if isinstance(item, list):
            double_list(item)
    pass


if __name__ == '__main__':
    lst = [1, [4, 6.3], True]
    double_list(lst)
    print(lst)

# enumerate(iteration,start)函数，默认包含两个参数，iteration是指需要遍历的参数，start是指从该参数开始枚举，默认start为0,那就是从0开始遍历
b = [1, 3, 4, 5, 67, 889, "a", 'f']
for index, item in enumerate(b, 2):
    print(index, item)

# isinstance()函数用来判断一个对象是否是已知的类型
# instance(object,classinfo)
