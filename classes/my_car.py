'''
@File    :   my_car.py
@Time    :   2022/05/26 20:27:23
@Author  :   Liuanglin
@Desc    :   
'''

'''
导入类
from mudule import Class
导入类后即可创建该类实例
使用类中定义的方法
'''
from car import Car

my_new_car = Car('ifiniti', 'q50', '2020')
print(my_new_car.get_full_name())
