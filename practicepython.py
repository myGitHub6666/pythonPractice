a = 10
b = 20
c = a, b
print(type(c))
b, a = c
print(b, a)
x, y, z, a = [1, 2, 34, 4]
print(x, y, z, a)
x = 1
y = 2
z = 3
c = (x, y, z)
z, x, y = c
print(z, x, y, '<<<<')
x, y, z = (1, 2, 4)
print(x, y, z)
#  组包:将多个数值使用逗号连接，组成元组的过程叫组包
# 拆包：将容器中的数据使用多个变量分别保存的过程，注意，变量的个数要和容器的个数保持一致
g_num = 10


def fun1():
    print(f'引用全局变量：{g_num}')


def fun2():
    g_num = 20
    print(f"定义局部变量：{g_num}")


def fun3():
    global g_num
    g_num = 30
    print(f"把全局变量的值修改为：{g_num}")


fun1()
fun2()
fun3()


# 函数返回多个返回值
def fun4(a, b):
    num1 = a + b
    num2 = a - b
    return num1, num2


# 用元组这个变量进行接收，然后再分别取值
rel = fun4(10, 4)
print(rel, rel[0], rel[1])
# 直接进行拆包赋值
x, y = fun4(10, 5)
print(x, y)


# 传参的方式一般使用位置传参。位置传参必须按照顺序，另外还有关键字传参，如果位置传参和关键字传参混合使用，那关键字传参必须写在位置传参的后面

def fun5(a, b, c):
    print(f"a={a},b={b},c={c}")


# 位置传参
fun5(1, 2, 3)
# 关键字传参，顺序可以任意写
fun5(a=2, c=4, b=5)
# 混合传参，关键字传参必须写在位置参数的后面
fun5(1, 2, c=2)


# 缺省参数，有一个好处就是，如果传递实参的值，那么就使用实参的值，如果不传递实参的值，那就是用默认的值
def show_info(name, sex='保密'):
    print(name, sex)


show_info('lucy', '女')  # lucy 女
show_info('lily')  # lily, 默认


# 不定长参数分为两种，一种是不定长位置参数，即是元组，
# 先把普通位子参数的个数排除掉，下来就是不定长参数
def ret(a, b, *args):
    print(a, b, args)
    print(type(args))
    print(a, b, len(args))


ret(1, 2, 1, 2, 3, 4)


# 不定长关键字参数，所传入的数据，保存下字典中
def ret1(a, b, *args, c, d, **kwargs):
    print(f"a={a},b={b},agrs={args},c={c},d={d},kwgrgs={kwargs}")


ret1(1, 2, 3, 5, 6, c=7, d=8, name='lucy', sex='女') # a=1,b=2,agrs=(3, 5, 6),c=7,d=8,kwgrgs={'name': 'lucy', 'sex': '女'}

# sep是多个位置参数之间的间隔，end为函数结束后，都会换行默认是end='/n'
print(1,2,sep='-',end='  ')
print(1,2,sep='  ')

# 类
class Mouth_M():
    #  类中的函数，第一个参数必须是self，就是对象本身
    def number(self):
        pass