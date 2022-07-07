'''
@File    :   ordinal_numbers.py
@Time    :   2022/05/03 15:10:42
@Author  :   Liuanglin
@Desc    :   序数-序数代表位置
大多数序数是以 th 结尾
除了 1 2 3 1st 2nd 3rd
创建一个列表存储1-9的数字
遍历列表
使用 if-elif-else 链 打印序数
'''

numbers = []
for number in range(1, 10):
    numbers.append(number)
print(numbers)

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
