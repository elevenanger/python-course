'''
@File    :   class_instances.py
@Time    :   2022/05/19 20:05:22
@Author  :   Liuanglin
@Desc    :   可以直接修改类中的属性或者定义方法来变更类中的属性
'''

class Car:
    
    def __init__(self,brand,model,year) :
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
    def get_full_name(self) :
        return f'{self.brand.title()} {self.modle.title()}'
    
    def read_odometer(self) :
        print(f"The car has {self.odometer_reading} miles on it.")
    
    def adjust_miles(self,miles) :
        if miles < self.odometer_reading :
            print('this is illegal operation')
        else : self.odometer_reading = miles
        
    def drive(self,miles) :
        self.odometer_reading += miles

my_car = Car('infiniti','q50','2020')

print(my_car.get_full_name())

my_car.read_odometer()

'''
通过对实例访问属性，直接对属性进行赋值
instance.attr = val
'''
my_car.odometer_reading = 100
my_car.read_odometer()

'''
使用方法设置属性值
'''
my_car.adjust_miles(1000)
my_car.read_odometer()

'''
在方法中对属性值进行修改
'''
my_car.drive(10)
my_car.read_odometer()