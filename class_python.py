# 1 房子有户型，总面积，家具列表。新房没有任何家具
# 2 家具，有名字和占地面积，其中，席梦思占地面积4平米，衣柜占地面积2平米，餐桌占地面积1.5平米
# 3 将以上三件家具添加到房子中
# 4 打印房子是要求输出：户型，总面积，剩余面积，家具名称列表
# 5 在创建房子对象的时候，定义一哥剩余面积，初始面积等于剩余面积
# 6 当调用add_item方法的时候，向房间添加家具，让剩余面积-=家具面积
class House():
    def __init__(self, sharp, total_area):
        self.sharp = sharp
        self.total_area = total_area
        self.free_area = total_area
        # 新房子的家具列表是空的
        self.HouseItem = []

    def __str__(self):
        return f'户型为：{self.sharp},总面积为：{self.total_area},剩余面积为：{self.free_area},家具列表为：{self.HouseItem}'

    def add_item(self, item):
        # 添加家具的时候先判断一下，剩余面积家具的关系
        if self.free_area > item.area:
            self.HouseItem.append(item.name)
            self.free_area -= item.area
        else:
            print(f"剩余面积{self.free_area}不够放家具，麻烦换大房子")
        pass


class Item():
    def __init__(self, name, area):
        self.name = name
        self.area = area


house = House('三室一厅', 150)
bed = Item('席梦思',4)
chest = Item('衣柜',148)
house.add_item(bed)
house.add_item(chest)
print(house)
