# 将int数据类型转化字符串
def my_str(int_value):
    """
    将int_value转换成字符串
    1,获得某一个位数的数字之后，可以通过字典获得相应的字符串，也可以通过ascil码来获取对应的字符串
    2,如果传入的是0，则返回字符串’0‘
    3,如果传入的参数是负数，需要标记记录，最后在列表的APPend一个’-'的字符串
    4,lst =[1,2,3]，想要反转，lst =[3,2,1]
    :param int_value:
    :return:
    """
    # 定义一个字典，数字为键，字符串为值
    dic = {
        0:'0',
        1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9'
    }
    # 设定一个状态，就是值是否为负数的状态，因为后面要判断是不是负数，所以要用一下
    int_value_is_zhengshu = True
    if int_value < 0:
        int_value_is_zhengshu = False
        int_value = abs(int_value)
    lst =[]
    # int_value 只要不是0就是True。
    # 布尔类型（bool）只有两个值，分别是 True 和 False，Python 会把 True 当做“真”，
    # 把 False 当做“假”。
    # 对于数字，Python 会把 0 和 0.0 当做“假”，把其它值当做“真”。
    # 对于其它类型，当对象为空或者为 None 时，Python 会把它们当做“假”，其它情况当做真
    while int_value:
        # 取出余数，即使最后一位
        num = int_value % 10
        # 把商值赋值给int_value。
        int_value = int_value // 10
        # 通过字典把数字转化为字符串，然后加入到列表中
        lst.append(dic[num])
    # 判断是否是负数，如果是负数，就要加上'-'符号
    if  not int_value_is_zhengshu:
        lst.append('-')
    # 对列表进行反转
    lst = lst[::-1]
    # 然后用空字符join这个列表，就可以把列表转化为字符串。并返回
    return ''.join(lst)


if __name__ == '__main__':
    print(my_str(-123)+my_str(3))