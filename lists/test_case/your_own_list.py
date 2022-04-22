'''
@File    :   your_own_list.py
@Time    :   2022/04/21 21:57:23
@Author  :   Liuanglin
@Desc    :   
创建一个你最喜欢的交通工具的 list
为这个 list 中的元素打印相关的宣言
'''

from email import message


transportation = ['car','airplane','tank','tractor'] 
message = f'I wanna have a {transportation[0]}'
print(message)
message = f'Take a {transportation[1]} to faraway'
print(message)
message = f'Build a {transportation[2]}'
print(message)
message = f'Use my {transportation[-1]}'
print(message)