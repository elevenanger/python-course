'''
@File    :   odd_numbers.py
@Time    :   2022/04/24 21:18:00
@Author  :   Liuanglin
@Desc    :   创建一个只包含 1，20 中奇数的列表
使用 for 遍历打印列表
'''

odd_numbers = list(range(1, 20, 2))
for number in odd_numbers:
    print(number)
