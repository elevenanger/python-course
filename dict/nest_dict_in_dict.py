'''
@File    :   nest_dict_in_dict.py
@Time    :   2022/05/08 17:01:57
@Author  :   Liuanglin
@Desc    :   字典嵌套字典
'''

zhao = {
    'name' : 'Zhao',
    'index' : 1,
}

qian = {
    'name' : 'Qian',
    'index' : 2,
}

sun = {
    'name' : 'Sun',
    'index' : '3',
}

li = {
    'name' : 'li',
    'index' : '4',
}

surnames = {
    '1st' : zhao,
    '2nd' : qian,
    '3rd' : sun,
    '4th' : li,
}

for k,v in surnames.items() :
    print (f"name {v['name']}")
    print (f"index {v['index']}")