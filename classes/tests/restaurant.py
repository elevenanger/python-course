'''
@File    :   restaurant.py
@Time    :   2022/05/18 21:14:16
@Author  :   Liuanglin
@Desc    :   创建一个名为 Restaurant 的类
__init__() 方法需要有两个属性 restaurant_name 和 cuisine_type 
定义一个方法名为 describe_restaurant() 打印这两个属性的信息
定义一个 open_restaurant() 方法表示饭店已经开门
创建该类实例
打印属性信息
调用每个方法
'''


class Restaurant :
    
    def __init__(self,restaurant_name,cuisine_type) :
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self) :
        print(f"{self.restaurant_name} cooking {self.cuisine_type}")
    
    def open_restaurant(self) :
        print(f"{self.restaurant_name} open for business!")
        
peace_restaurant = Restaurant('peace restaurant','Chinese Food')

print(peace_restaurant.restaurant_name)
print(peace_restaurant.cuisine_type)

peace_restaurant.describe_restaurant()
peace_restaurant.open_restaurant()