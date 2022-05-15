'''
@File    :   city_names.py
@Time    :   2022/05/15 19:45:07
@Author  :   Liuanglin
@Desc    :   定义一个函数名为 city_names()
使用城市名和国家作为参数调用该函数
返回格式 "city,country"
调用函数三次，打印信息
'''

location = []

def city_names(city,country = 'china') :
    return f'"{city.title()}, {country.title()}"'

location.append(city_names('chang sha'))
location.append(city_names(city='wu han'))
location.append(city_names(city='chicago',country='american'))

while location :
    print(location.pop())