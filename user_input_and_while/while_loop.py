'''
@File    :   while_loop.py
@Time    :   2022/05/08 19:16:29
@Author  :   Liuanglin
@Desc    :   while 循环只要循环的条件为 true 就会一直执行循环内的代码
'''

'''
while condition :
    do something
'''
number = 0
while number < 10:
    number += 1
    print(number)

'''
为 while 循环添加退出条件
'''
prompt = 'say something '
msg = ''
while msg != 'quit':
    msg = input(prompt)
    print(f'\n{msg}')
