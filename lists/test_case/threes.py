'''
@File    :   threes.py
@Time    :   2022/04/24 21:20:16
@Author  :   Liuanglin
@Desc    :   创建一个3,30所有数字的三倍的列表
for 循环打印每一个数字
'''

numbers = [value * 3 for value in range(3, 31)]
for number in numbers:
    print(number)
