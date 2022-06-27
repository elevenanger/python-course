# @File  : name_function.py
# @Author: liuanglin
# @Time: 2022/6/20 22:15 
# -*- coding: utf-8 -*-

def get_formatted_name(first, last, middle=''):
    if middle:
        fullname = f"{first} {middle} {last}"
    else:
        fullname = f"{first} {last}"
    return fullname.title()
