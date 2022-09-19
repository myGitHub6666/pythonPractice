# 使用input函数接收用户的输入，
# 如果输入的数据不可以转换成int类型数据，则输出"无法使用int函数转换"，
# 如果可以，则将用户的输入转成int类型数据并继续判断。
# 如果输入数据是奇数，则将其乘以2并输出，
# 如果是偶数，则判断是否能被4整除，
# 如果可以则输出被4整除后的值，
# 若不能被4整数，则判断是否大于20，如果大于20则输出与20的差值，
# 如果小于等于20，则直接输出该值
value = input('>>>')
if not value.isdigit():
    print('无法使用int函数转化')
else:
    if int(value) %2 ==0:
        if int(value) % 4 ==0:
            print(int(value)/4)
        else:
            if int(value)>20:
                print(int(value)-20)
            else:
                print(int(value))
    else:
        a = int(value) * 2
        print(a)
# str(a).isdigit()函数 可以判断字符串str(a)是不是全部由数字组成。如果全是数字返回True，否则返回False
