'''
@File    :   number_served.py
@Time    :   2022/05/19 20:35:16
@Author  :   Liuanglin
@Desc    :   基于 Restaurant 类
新增一个属性 number_served 默认值为 0
创建实例
打印餐馆预留的席位
改变它的值，并再次打印
添加方法 set_number_served() 设置保留席位
调用该方法并打印预留的席位
添加方法 increment_number_served() 增加预留的席位
调用方法并打印预留的席位
'''


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('he ping', 'chinese food')
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)
