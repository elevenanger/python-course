# @File  : addition_calculator.py
# @Author: liuanglin
# @Time: 2022/6/8 21:11 
# -*- coding: utf-8 -*-

# 基于 addtion.py 中的函数
# 使用 while 循环直到用户输入了数字

def input_number():
    number = input('请输入数字 : ')
    try:
        int_number = int(number)
    except ValueError:
        print(f'{number} 不是数字，请重新输入')
    else:
        print(int_number)
        return int_number


while True:
    num = input_number()
    if num:
        break
