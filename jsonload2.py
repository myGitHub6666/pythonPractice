# 提取json数据中的用户名，密码，和预期结果，组成如下格式【（），（），（）】，自动化所需要的参数
import json


# 定义一个把json数据进行转换的函数
def getdate():
    list1 = []
    with open('data.json', encoding="utf_8") as f:
        # 获取到的数据是列表形式
        res = json.load(f)
        # 遍历列表
        for i in res:
            tuple1 = (i.get("desc"), i.get("username"), i.get("password"))
            list1.append(tuple1)
    return list1


if __name__ == "__main__":
    print(getdate())
