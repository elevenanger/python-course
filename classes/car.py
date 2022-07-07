'''
@File    :   car.py
@Time    :   2022/05/26 20:38:22
@Author  :   Liuanglin
@Desc    :   模块-可以将多个类放在同一个模块中
'''


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.modle = model
        self.year = year
        '''
        里程表读数
        实例化对象时默认为 0
        因为该属性有默认值
        所以无需在实例化时传参进行赋值
        '''
        self.odometer_reading = 0

    '''
    在方法中使用对象实例的属性
    '''

    def get_full_name(self):
        return f'{self.brand.title()} {self.modle.title()}'

    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it.")

    def adjust_miles(self, miles):
        if miles < self.odometer_reading:
            print('this is illegal operation')
        else:
            self.odometer_reading = miles

    def drive(self, miles):
        self.odometer_reading += miles


class Battery:

    def __init__(self, battery_size=90):
        self.battery_size = battery_size

    def desc_battery(self):
        print(f"{self.battery_size} kWh battery.")

    def get_range(self):
        range = self.battery_size * 10
        print(f'The battery range {range} miles.')
        return range

    def charge(self):
        self.battery_size += 20


class ElectricCar(Car):

    def __init__(self, make, modle, year):
        super().__init__(make, modle, year)
        self.battery = Battery()
