'''
@File    :   restaurant_module.py
@Time    :   2022/05/26 20:58:43
@Author  :   Liuanglin
@Desc    :   将 Restaurant 类放在一个单独的 module 中
创建独立的文件从 module 中导入 Restaurant 类
创建实例
调用 Restaurant 方法
'''


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} cooking {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} open for business!")
