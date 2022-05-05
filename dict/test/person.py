'''
@File    :   person.py
@Time    :   2022/05/04 20:12:57
@Author  :   Liuanglin
@Desc    :   使用字典储存一个你知道的人的信息
包括 ： 姓、名、居住城市，并打印其中的所有信息
'''

bat_man = {
    'first_name' : 'Bruce',
    'last_name' : 'Wayne',
    'living_city' : 'Gotham',
}

print(bat_man['first_name'])
print(bat_man.get('last_name'))
print(bat_man.get('living_city'))