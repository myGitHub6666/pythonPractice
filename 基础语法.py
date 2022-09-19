# 使用input函数接收用户的输入
# 如果用户输入的整数是偶数，则使用print函数输出"你输入的整数是:{value}, 它是偶数",
# {value}部分要替换成用户的输入。
value = int(input('>>>'))
if value % 2 == 0:
    print(f'你输入的整数是：{value},他是偶数')
else:
    print(F'你输入的{value}是奇数')
# 使用input函数接收用户的输入数据，
# 如果用户输入python，则输出90，
# 如果用户输入java,输出95，
# 如果用户输入php，输出85，
# 其他输入，程序输出0
# 应该每个条件之间都是互斥的，所以用if elif else
value1 = input('>>>>')
if value1 == 'python':
    print(90)
elif value1 =='java':
    print(95)
elif value1 == 'php':
    print(85)
else:
    print(0)
