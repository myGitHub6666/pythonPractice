# 将'xx.xx'的字符串转化为xx.xx的小数
import str_int


def my_float(string):
    '''
    1,先将字符串按照'.'进行分割，分割成整数部分和小数部分。
    2 ,然后分别对整数部分，和小数部分进行转化，调用str——int函数
    3， 小数部分的要一直乘以0.1 直到小数部分的数据小于1
    4 然后把两部分进行相加
    :param string:
    :return:
    '''
    lst = string.split('.')
    num1 = str_int.my_int(lst[0])
    num2 = str_int.my_int(lst[1])
    while num2 >=1:
        num2 = num2 * 0.1
    num = num1 + num2
    return num


if __name__ == '__main__':
    print(my_float('1.1')+1)
