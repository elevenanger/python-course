'''
@File    :   favorite_fruit.py
@Time    :   2022/05/03 14:08:05
@Author  :   Liuanglin
@Desc    :   创建一个水果列表，写一系列的 if 语句检查某个水果是否在列表中
1、三个水果 favorite_fruits
2、五个独立的 if 语句，检查某个水果是否在列表中
'''

favorite_fruits = ['grape','pear','peach']
fruits = ['apple','lychee','grape','peach','banana']
for fruit in fruits :
    if fruit in favorite_fruits :
        print(f'you really like {fruit} !')
    else:
        print(f'you do not like {fruit} .')