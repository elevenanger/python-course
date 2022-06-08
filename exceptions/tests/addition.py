# @File  : addition.py
# @Author: liuanglin
# @Time: 2022/6/8 21:06 
# -*- coding: utf-8 -*-

# 提示输入数字 但是用户确输入了文本
# 这时候程序会抛出异常
# 捕获这个异常
# 并给用户友好的提示

def input_number():
    number = input('请输入数字 : ')
    try:
        int_number = int(number)
    except ValueError:
        print(f'{number} 不是数字，请重新输入')
    else:
        print(int_number)
        return int_number


input_number()
