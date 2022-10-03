import random


class Game:
    top_score = 0

    def __init__(self, name):
        # 定义实例属性name
        self.name = name

    @staticmethod
    def show_help():
        print('这是帮助文档')

    @classmethod
    def show_top_score(cls):
        print(f"游戏的最高分是:{cls.top_score}")

    def start_game(self):
        print(f"{self.name}开始一局游戏，游戏中。。。。", end='')
        # 本次游戏的得分
        score = random.randint(10, 100)
        print(f'本次游戏的分数是：{score}')
        if score > Game.top_score:
            # 修改最高分
            Game.top_score = score


xl = Game('小李')
xl.start_game()
xl.show_top_score()
xl.start_game()
xl.show_top_score()
xl.show_help()
