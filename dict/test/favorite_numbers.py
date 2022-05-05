'''
@File    :   favorite_numbers.py
@Time    :   2022/05/04 20:19:37
@Author  :   Liuanglin
@Desc    :   使用字典存储人们最喜欢的数字 5个
'''

names_and_number = {
    'zhao' : 4,
    'qian' : 0,
    'sun' : 3,
    'li' : 1,
    'wang' : 5,
}
print(f"zhao's favorite number is {names_and_number['zhao']}")
print(f"qian's favorite number is {names_and_number['qian']}")
print(f"sun's favorite number is {names_and_number['sun']}")
print(f"li's favorite number is {names_and_number['li']}")
print(f"wang's favorite number is {names_and_number.get('wang')}")