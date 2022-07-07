'''
@File    :   cars.py
@Time    :   2022/05/16 22:08:39
@Author  :   Liuanglin
@Desc    :   定义一个函数在一个字典中存储汽车的信息
函数固定接收制造商和型号
另外接收任意数量的关键字参数
'''


def make_car(brand, model, **other_info):
    car = {}
    car['brand'] = brand.title()
    car['model'] = model.title()
    for k, v in other_info.items():
        car[k] = v
    return car


my_car = make_car('infiniti', 'q50', color='blue', version='3rd')
print(my_car)
