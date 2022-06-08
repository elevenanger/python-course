# @File  : cats_and_dog.py
# @Author: liuanglin
# @Time: 2022/6/8 21:15 
# -*- coding: utf-8 -*-

# 创建两个文件 cat.txt dog.txt
# 分别存储至少三个名字
# 读取文件中的数据并输出到屏幕中
# 使用 try-except 代码块包裹逻辑
# 当文件不存在则提示文件不存在

def read_file(file):
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'{file} 不存在')


read_file('cats_and_dog.py')
read_file('cat.txt')
