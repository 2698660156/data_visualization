from random import randint  # 从random模块导入randint函数，用于生成随机数

class Die:
    """一个代表单个骰子的类。"""

    def __init__(self, num_sides=6):
        """初始化方法，默认为六面骰子。"""
        # 设置骰子的面数，默认为6
        self.num_sides = num_sides

    def roll(self):
        """模拟骰子的投掷，返回1到骰子面数之间的一个随机值。"""
        # 使用randint函数生成一个在1和self.num_sides之间的随机整数
        return randint(1, self.num_sides)