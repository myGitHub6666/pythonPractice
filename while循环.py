# 使用input函数接收用户输入的整数，
# 如果是偶数，则使用print函数输出"你输入的是一个偶数",
# 反之输出"你输入的是一个奇数"，
# 用户可以输入多次，直到输入quit时程序退出
# while True:
#     value = input('>>>')
#     if value == "quit":
#         break
#     elif int(value)%2 == 0:
#         print('你输入的是一个偶数')
#     else:
#         print('你输入的是一个奇数')
# 已知 lst = [2, 3, 4]
# 依次要求用户输入2，3，4 的整数倍，
# 先让用户输入2的倍数，如果用户输入的正确，输出“输入正确”，否则输出 “输入错误”，
# 如果用户输入quit，则停止当前的输入，让用户输入3的倍数，
# 输入3的倍数的过程中，如果用户输入quit，则让用户输入4的倍数
# 方法一
# lst =[2,3,4]
# for i in lst:
#     while True:
#         input_number = input(f'请输入{i}的倍数的数据或者quit:')
#         if input_number =='quit':
#             break
#         if int(input_number)%2==0:
#             print('输入正确')
#         else:
#             print('输入错误')
# 方法二
# lst = [2, 3, 4]
# for item in lst:
#     while True:
#         input_str = input("请输入{number}的倍数,想停止输入时，输入quit:".format(number=item))
#         if input_str == 'quit':
#             break
#         else:
#             continue # 加入continue可以跳出本层循环
#         number = int(input_str)
#         if number % item == 0:
#             print("输入正确")
#         else:
#             print("输入错误")
# 使用input函数接受用户的输入，
# 如果用户输入的数值小于等于10，则判断是奇数还是偶数，
# 如果数值大于10，则输出“输入大于10，不判断奇偶”,用户输入quit，结束程序
while True:
    input_word = input('>>>')
    if input_word == 'quit':
        break
    if int(input_word) > 10:
        print('输出大于10，不判断奇数偶数')
        continue
    if int(input_word) % 2 ==0:
        print('偶数')
    else:
        print('奇数')
