'''
@File    :   skill_base.py
@Time    :   2022/05/22 21:01:40
@Author  :   Liuanglin
@Desc    :   技能基类、父类
'''


class Skill:

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.initiative = False
        self.range = 300
        self.cool_down = 10

    def desc_skill(self, desc):
        return f"{self.name.title()} : {desc} "

    def cast_skill(self):
        print(f"{self.name.title()} hit {self.damage} !")


class Hero:

    def __init__(self, hero_name, skill_name, damage):
        self.name = hero_name
        # 在初始化函数中定义对象实例作为类的属性
        self.skill = Skill(skill_name, damage)
        self.rank = 1

    def hero_cast_skill(self):
        print(f"{self.name.title()}")
        # 使用作为属性的类中定义的方法
        self.skill.cast_skill()

    # 基于一个属性的值，调整另一个属性的值
    def adjust_hero_rank(self):
        if self.skill.damage > 100:
            self.rank = 2


wong = Hero('wong', 'break ice', 100)
wong.hero_cast_skill()
print(wong.rank)
wong.skill.damage = 200
wong.adjust_hero_rank()
print(wong.rank)
