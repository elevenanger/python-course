'''
@File    :   ultimate_skill.py
@Time    :   2022/05/22 21:11:28
@Author  :   Liuanglin
@Desc    :   终极技能类 继承技能类
'''

from skill_base import Skill

'''
定义子类
class ChildClass(ParentClass) :
子类将会继承父类的属性和方法
并且可以定义新的属性和方法

使用继承
可以使子类保留所需要的父类的属性和方法
重写不需要的
'''
class UltimateSkill(Skill) :
    
    def __init__(self, name, damage,addtion):
        '''
        super 关键字允许调用父类的方法以及使用父类的属性
        首先调用父类的 __init__() 方法
        初始化父类的属性和方法
        使得其可以在子类中使用
        '''
        super().__init__(name, damage)
        super().initiative = True
        # 定义新的属性
        self.addition = addtion
        
    # 定义和父类相同的方法名，重写父类的方法
    def cast_skill(self):
        print(f"{self.name.title()} cause {self.damage * self.addition} damage !")

kill_god = UltimateSkill('kill god',100,3)
kill_god.cast_skill()