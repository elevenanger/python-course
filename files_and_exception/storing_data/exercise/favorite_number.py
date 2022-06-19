# @File  : favorite_number.py
# @Author: liuanglin
# @Time: 2022/6/19 20:59 
# -*- coding: utf-8 -*-

"""

编写程序提示用户输入最喜欢的数字
存储到JSON文件中
编写另外一个独立的程序读取JSON文件中的数据
输出信息告诉用户你已经知道他最喜欢的数字是什么
"""
import json


def input_number():
    """输入数字"""
    number = input("输入你最喜欢的数字：")
    if number:
        return number
    else:
        input_number()


def store_number():
    """存储数字"""
    filename = 'favorite_number.json'
    number = input_number()
    with open(filename, 'w') as f:
        json.dump(number, f)


def get_store_number():
    """获取已存储的数字"""
    filename = 'favorite_number.json'
    try:
        with open(filename, 'r') as f:
            number = json.load(f)
            return number
    except FileNotFoundError:
        store_number()


def favorite_number():
    """打印最喜欢的数字"""
    number = None
    while number is None:
        number = get_store_number()
    print(f"你最喜欢的数字是：{number}")


favorite_number()
