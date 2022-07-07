'''
@File    :   favorite_places.py
@Time    :   2022/05/08 17:37:06
@Author  :   Liuanglin
@Desc    :   创建一个名为 favorite_places 字典
三个人名作为字典的 key 
每个人一到三个喜欢的地方
打印每个人的名字以及其喜欢的地方
'''

favorite_places = {
    'Zhao': ['Songshan Lake', 'Forrest Park', 'Humen'],
    'Qian': ['Xiang River', 'Yuelu mountain'],
    'Sun': ['Tian An Men'],
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"{name}'s favorite palces :")
        for place in places:
            print(f'\t{place}')
    else:
        print(f"{name}'s favorite place is {places[-1]}")
