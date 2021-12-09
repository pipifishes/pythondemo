from random import randint
'''
# print(Dice().roll_dice()): 访问随机到的随机整数
'''
class Dice:

    def __init__(self,num_sides=6):
        """骰子默认有6个面"""
        self.num_sides = num_sides

    def roll_dice(self):
        return randint(1,self.num_sides)


