'''
@File    :   rivers.py
@Time    :   2022/05/06 22:04:55
@Author  :   Liuanglin
@Desc    :   创建一个字典包含三个国家以及其主要的河流
1、使用循环打印河流
2、使用循环打印河流名
3、使用循环打印国家名
'''

rivers = {
    'china': 'huanghe',
    'brazil': 'amazon',
    'american': 'mississippi',
}

for country, river in rivers.items():
    print(f'{river.title()} in {country.title()}')

for country in rivers.keys():
    print(country.title())

for river in rivers.values():
    print(river.title())
