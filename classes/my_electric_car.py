'''
@File    :   my_electric_car.py
@Time    :   2022/05/26 20:39:12
@Author  :   Liuanglin
@Desc    :   将业务逻辑代码与模块或者类的定义分离
'''

'''
从模块中导入多个类
from module import Class1,...,Classn
'''
from car import Car, ElectricCar
# 导入整个模块
import car
# 导入模块中所有类
from car import *
# from module import Class as C 为导入类设置别名
from car import Car as C
from car import ElectricCar as EC

my_electric_car = ElectricCar('xiao peng', 'p7', '2022')
print(my_electric_car.get_full_name())
my_electric_car.battery.get_range()
my_electric_car.battery.charge()
my_electric_car.battery.get_range()

my_car = Car('ifiniti', 'q50', '2020')
my_car_alias = C('nissan', 'sunshine', '2015')

cars = []
cars.append(my_car)
cars.append(my_car_alias)
cars.append(my_electric_car)

for car in cars:
    print(car.get_full_name())
