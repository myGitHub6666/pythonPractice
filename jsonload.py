import json

# json的读取
with open("info1.json", encoding="utf-8") as f:
    info = json.load(f)
    # 得到的数据是list形式
    print(type(info))
    for i in info:
        print(i.get('name'),
              i.get('age'),
              i.get("isman"),
              i.get("address").get("city"))
