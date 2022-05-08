'''
@File    :   multiples_of_ten.py
@Time    :   2022/05/08 19:10:39
@Author  :   Liuanglin
@Desc    :   用户录入一个数字 检查这个数字是不是 10 的倍数

'''

msg = 'please input a number : '
number = int(input(msg))
if number != 0 and number % 10 == 0 :
    print(f"{number} is multiples of 10 ")
else :
    print(f"{number} is not multiples of 10 ")