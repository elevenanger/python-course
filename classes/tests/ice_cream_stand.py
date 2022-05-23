'''
@File    :   ice_cream_stand.py
@Time    :   2022/05/23 21:09:45
@Author  :   Liuanglin
@Desc    :   雪糕站是一种特殊的 Restaurant
定义一个名为 IceCreamStand 的类继承 Restaurant 类
新增一个 flavours 属性存储雪糕的口味列表
写一个方法来展示这些口味
创建实例调用该方法
'''

from restaurant import Restaurant
class IceCreamStand(Restaurant) :
    
    def __init__(self, restaurant_name, cuisine_type,flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    
    def display_flavours(self) :
        print(f"{self.restaurant_name.title()} flavours: ")
        for flavour in self.flavours :
            print(f"\t{flavour}")

ice_cream_flavours = ['vanilla','galliano','rum']
mcm_ice_cream_stand = IceCreamStand('MacDonald','fast food',ice_cream_flavours)
mcm_ice_cream_stand.display_flavours()