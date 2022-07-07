'''
@File    :   modulo.py
@Time    :   2022/05/08 18:48:23
@Author  :   Liuanglin
@Desc    :   取模运算符 %
'''

'''
num1 % num2 
取模运算
'''
numbers = [11, 23, 43, 545, 12]
for num in numbers:
    remainder = num % 2
    if (remainder == 1):
        print(f"{num} is an odd number ")
    else:
        print(f"{num} is an even number ")
