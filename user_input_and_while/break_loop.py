'''
@File    :   break_loop.py
@Time    :   2022/05/08 20:03:45
@Author  :   Liuanglin
@Desc    :   使用 break 语句结束循环
'''

'''
while condition :
    do something 
    break
    do something else
使用 break 语句即刻退出整个循环
不执行 break 语句后面的代码
'''
prompt = 'say something : '
while True :
    msg = input(prompt)
    if msg == 'quit' :
        break
    else :
        print(msg)
# break 语句可以使用在 Python 任意的循环中，包括 for 循环
for number in range(20) :
    if number == 10 :
        break
    else :
        print(number)