'''
@File    :   pets.py
@Time    :   2022/05/08 17:29:43
@Author  :   Liuanglin
@Desc    :   创建多个字典
每个描述一个宠物
包括宠物类型和主人的名字
将其存储在一个名为 pets 的列表中
遍历列表，打印每个宠物所有的信息
'''


pikachu = {
    'name' : 'Pikachu',
    'owner' : 'Zhi',
}

meowth = {
    'name' : 'Meowth',
    'owner' : 'James',
}

pets = [pikachu,meowth]

for pet in pets :
    print(f"Name {pet['name']}")
    print(f"Owner {pet['owner']}")