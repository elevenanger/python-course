'''
@File    :   lottery.py
@Time    :   2022/05/27 20:49:39
@Author  :   Liuanglin
@Desc    :   抽奖程序
创建一个 list 或者 tuple 
包括 10 个数字和 5 个字母
从中随机选取四个元素
打印出来
'''

from random import randint

class Lottery :
    
    def __init__(self) :
        self.lottery_pocket = self.__init__pocket()
        
    def __init__pocket(self) :
        lottery_pocket = ['a','b','c','d','e']
        for number in range(10) :
            lottery_pocket.append(number)
        return lottery_pocket
    
    def draw(self,draw_number=4) :
        draw_pocket = self.lottery_pocket[:]
        prized = []
        time = 0
        while time < draw_number :
            pop_number = randint(0,len(draw_pocket)-1)
            prized.append(draw_pocket.pop(pop_number))
            time += 1
        print(prized)
        return prized
    
    def continuous_draw(self,times=1,draw_number = 4) :
        time = 0
        while time < times :
            self.draw(draw_number=draw_number)
            time += 1
    
    def prized_ticket(self,ticket_numbers) :
        count = 0
        prized = False
        while not prized:
            prized = (ticket_numbers == self.draw())
            count += 1
        print(count)
        return

lot = Lottery()
lot.continuous_draw(10)
ticket = [1,'a',2,'c']
lot.prized_ticket(ticket)