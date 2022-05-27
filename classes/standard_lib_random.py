'''
@File    :   standard_lib_random.py
@Time    :   2022/05/27 20:26:57
@Author  :   Liuanglin
@Desc    :   使用 Python 的标准库
'''

from random import randint,choice

for number in range(10) :
    print(randint(1,10))

names = ['dada','bibi','cici','qiqi']
name = choice(names)
print(name)