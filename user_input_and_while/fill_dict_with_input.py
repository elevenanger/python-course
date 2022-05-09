'''
@File    :   fill_dict_with_input.py
@Time    :   2022/05/09 21:19:42
@Author  :   Liuanglin
@Desc    :   使用字典收集用户输入的信息
'''

questionnair = {}

active = True

while active :
    name = input("What's your name : ")
    age = input("How old are you : ")
    questionnair[name] = int(age)
    if questionnair[name] > 30 :
        active = False

for name ,age in questionnair.items() :
    print(f'{name} is {age} years old')