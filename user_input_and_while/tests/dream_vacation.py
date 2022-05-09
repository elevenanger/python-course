'''
@File    :   dream_vacation.py
@Time    :   2022/05/09 21:47:53
@Author  :   Liuanglin
@Desc    :   调查用户假期想去的地方 打印所有调查结果
'''

dream_vacations = {}
active = True

while active :
    name = input("What's your name : ")
    place = input("What's your dream place : ")
    if place == 'nowhere' :
        break
    dream_vacations[name] = place

for name , place in dream_vacations.items() :
    print(f"{name}'s dream place is {place}")