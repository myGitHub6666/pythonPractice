# abs()函数 返回数字绝对值
def my_abs(number):
    '''
    对传入的参数进行判断，判断是否是数字类型，一般float和int比较常用。
    判断变量的类型，可以使用isinstance函数，该函数的第一参数是要检查的类型的对象，第二个参数是数据类型
    也可以是一个元祖，元祖里有多个数据类型，只要满足其中一个就返回True
    如果数值小于0，可以乘以-1就可以得到绝对值
    :return:
    '''
    if isinstance(number, (int, float)):
        if number < 0:
            number *= -1
            return number # 如果小于0  返回值*-1
        else:
            return number
    else:
        return number # 当不符合数字类型的时候，要把数据进行返回
# print(my_abs(1))


def my_abs1(number):
    if not isinstance(number, (float, int)):
        return number # 如果不是数字是真的，那就直接返回number。以下的语句就不执行了
    if number < 0:
        number *= -1
    return number

# 如果在别的模块中被导入，本段不执行。当模块被直接执行时候，此处为真。
if __name__ == '__main__':
    print(my_abs1('jhjk'))
    print(my_abs1(-3.9))
    print(my_abs1(154.3))
