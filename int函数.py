# 内置函数int，可以将float,全是数字的字符串转成int类型的数据，
# 为了降低难度，这个练习题只要求你实现其中一种功能，
# 将全是由数字组成的字符串转成int类型数据，
# 例如将字符串"432" 转成整数432，函数定义如下
def my_int(string):
    """
    将字符串string转成int类型数据
    不考虑string的类型,默认就是符合要求的字符串
    传入字符串"432" 返回整数432
    :param string:
    :return:
    """
    str_dic = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    count = 0
    ii = 1
    for i in string[::-1]:
        int_str = str_dic[i]
        count = count + int_str * ii
        ii *= 10
    return count


print(my_int('786587'))
