'''
@File    :   battery_upgrade.py
@Time    :   2022/05/23 21:31:10
@Author  :   Liuanglin
@Desc    :   定义汽车类
定义 电池 类
将电池作为汽车的一个属性
'''

class Car :
    def __init__(self,make,model,year) :
        self.make = make
        self.model = model
        self.year = year
    def desc_car(self) :
        print(f"{self.make.title()} {self.model.title()} {self.year}")

class ElectricCar(Car) :
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def get_range(self):
        print(f"剩余行驶里程： {self.battery.battery_size * 10 } 公里")

class Battery :
    def __init__(self,battery_size = 70) :
        self.battery_size = battery_size
    
    def charge(self) :
        self.battery_size += 10

xiao_peng_p7 = ElectricCar('xiao peng' ,'p7',2020)
xiao_peng_p7.get_range()
xiao_peng_p7.battery.charge()
xiao_peng_p7.get_range()
