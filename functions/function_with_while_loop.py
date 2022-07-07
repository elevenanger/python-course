'''
@File    :   function_with_while_loop.py
@Time    :   2022/05/15 19:35:03
@Author  :   Liuanglin
@Desc    :   在函数中使用循环
'''


def person_info_collection(limit=3):
    circle_number = 0
    persons = {}
    while circle_number < limit:
        person = {}
        name = input('input your name : ')
        age = input('input your age : ')
        person['name'] = name.title()
        person['age'] = age
        persons[circle_number] = person
        circle_number += 1
    print(persons)


person_info_collection(limit=5)
