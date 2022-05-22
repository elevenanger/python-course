'''
@File    :   skill_base.py
@Time    :   2022/05/22 21:01:40
@Author  :   Liuanglin
@Desc    :   技能基类、父类
'''

class Skill :
    
    def __init__(self,name,damage) :
        self.name = name
        self.damage = damage
        self.initiative = False
        self.range = 300
        self.cool_down = 10
        
    def desc_skill(self,desc) :
        return f"{self.name.title()} : {desc} "
    
    def cast_skill(self) :
        print(f"{self.name.title()} hit {self.damage} !")