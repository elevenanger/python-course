'''
@File    :   people.py
@Time    :   2022/05/08 17:20:50
@Author  :   Liuanglin
@Desc    :   创建两个字典 每个描述一个人物
将全部字典都存储在一个名为 people 的字典中
遍历字典 打印每一个人的所有信息
'''

kg = {
    'first_name' : 'Kevin',
    'last_name' : 'Garnnet',
    'team' : 'Celtics',
}

aj = {
    'first_name' : 'Michael',
    'last_name' : 'Jordan',
    'team' : 'Bulls',
}

people = {
    'aj' : aj,
    'kg' : kg,
}

for  k ,v in people.items() :
    print(f"{v['first_name']} {v['last_name']} take the championship in {v['team'].title()}")
