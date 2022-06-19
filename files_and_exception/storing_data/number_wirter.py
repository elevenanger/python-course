# @File  : number_wirter.py.py
# @Author: liuanglin
# @Time: 2022/6/9 21:08 
# -*- coding: utf-8 -*-


import json

# 使用 JSON 库写 JSON 写入可写入的对象
# json.dump()
numbers = [1, 2, 3, 4, 5]
number_file = 'numbers.json'
with open(number_file, 'w') as f:
    json.dump(numbers, f)

with open(number_file, 'r') as f:
    # json.load 读取 JSON 数据
    number = json.load(f)
    print(number)

user_name = 'username.json'
try:
    with open(user_name, 'r') as f:
        name = json.load(f)
except FileNotFoundError:
    name = input('输入您的姓名 ： ')
    with open(user_name, 'w') as f:
        json.dump(name, f)
else:
    print(f'hello, {name.title()}')
