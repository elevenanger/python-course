'''
@File    :   cities.py
@Time    :   2022/05/08 17:51:34
@Author  :   Liuanglin
@Desc    :   创建一个名为 cities 的字典
使用三个城市名作为 key
保存城市的信息 位置 人口 关键字
'''

cities = {
    'Chang Sha' : {
        'location' : 'South',
        'population' : 100_479_00,
        'fact' : 'star city',
    },
    'Bei Jing' : {
        'location' : 'North',
        'population' : 215_360_00,
        'fact' : 'capital',
    },
    'Chong Qing' : {
        'location' : 'West',
        'population' : 745_760_0,
        'fact' : 'mountain city',
    }
}

for city,info in cities.items() :
    print(city.upper())
    for k,v in info.items() :
        print(f"\t{k}\t{v}")