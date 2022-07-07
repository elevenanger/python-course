'''
@File    :   programming_poll.py
@Time    :   2022/05/29 20:57:44
@Author  :   Liuanglin
@Desc    :   编程投票
写一个 while 循环询问用户喜欢编程的原因
每个用户写一个原因
将他们的原因添加到文件中
'''

file_name = 'programming_poll.txt'

with open(file_name, 'a') as file_obj:
    while True:
        reason = input('why you like programming : ')
        if reason == 'quit': break
        file_obj.write(f'{reason}\n')
