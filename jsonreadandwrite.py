# 导包
import json
# 打开json
with open('dict.json',encoding= 'utf-8') as f:
    # 普通文件读取
    # buf = f.read()
    # print(type(buf),buf) 获取的是字符串形式的数据
    # 采用json的特殊方法读取
    res = json.load(f)
    # 获取到的是字典形式的数据
    print(type(res),res)
    # get('like')得到的是列表，然后取列表第一位
    print(res.get('like')[0])
    # get('address')得到的是字典，然后再获取city的值
    print(res.get('address').get('city'))



