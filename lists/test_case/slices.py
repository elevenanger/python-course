'''
@File    :   slices.py
@Time    :   2022/04/24 21:55:34
@Author  :   Liuanglin
@Desc    :   
创建一个列表
分别打印
前三个元素
中间三个元素
最后三个元素
'''

numbers = list(range(9))
print(f'first three element : {numbers[:3]}')
print(f'middle number : {numbers[3:6]}')
print(f'last three : {numbers[-3:]}')
