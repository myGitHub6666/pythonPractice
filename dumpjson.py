# json的写入
import json

my_list = [('正确的用户名和密码', 'admin', '123456'), ('错误的用户名', 'root', '123456'), ('错误的密码', 'admin', '123123')]
with open('info3.json', 'w', encoding='utf-8') as f:
    # json.dump(python中的数据类型，文件对象）
    # 把数据my_list写入文件，默认中文是按照ascii码的形式显示
    # json.dump(my_list, f)
    # 把默认的ascii码显示改为中文显示
    # json.dump(my_list,f,ensure_ascii=False)
    # 显示缩进
    json.dump(my_list, f, ensure_ascii=False, indent=4)
with open('info3.json', encoding='utf-8') as ff:
    list1 = json.load(ff)
    for i in list1:
        for ii in i:
            print(ii,end=" ")
        print(end='\n')
# 获取数据
# 正确的用户名和密码 admin 123456
# 错误的用户名 root 123456
# 错误的密码 admin 123123
