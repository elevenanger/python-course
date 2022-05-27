'''
@File    :   dice.py
@Time    :   2022/05/27 20:38:05
@Author  :   Liuanglin
@Desc    :   创建一个名为 Die 的类（骰子）
属性为 sides 
默认值为 6
定义一个方法 roll_die() 打印 1-sides 之间的一个随机数
创建一个6面骰子
roll 10次
再分别创建 10 面骰和 20 面骰
分别 roll 10次
'''

from random import randint

class Die :
    
    def __init__(self,sides=6) :
        self.sides = sides
    
    def roll_dice(self) :
        print(randint(1,self.sides))
    
    def roll_dice_times(self,time) :
        print(f"roll {self.sides} sides dice {time} times")
        index = 0
        while index < time:
            self.roll_dice()
            index += 1
        
six_sides_dice = Die()
six_sides_dice.roll_dice_times(10)
ten_sides_dice = Die(10)
ten_sides_dice.roll_dice_times(10)
twenty_sides_dice = Die(20)
twenty_sides_dice.roll_dice_times(10)