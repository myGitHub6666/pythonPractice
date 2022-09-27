# self就是对象本身
class Cat():
    def eat(self):
        print(f"{id(self)},{self.name}爱吃鱼")


red_cat = Cat()
red_cat.name = '红猫'
red_cat.eat()
print(f"{id(red_cat)}")
