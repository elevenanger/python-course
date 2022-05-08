'''
@File    :   flag.py
@Time    :   2022/05/08 19:41:19
@Author  :   Liuanglin
@Desc    :   使用标识判定 while 循环的退出条件
'''

'''
一个程序仅在很多条件都为 True 的情况下运行
可以定义一个变量决定整个程序是否为活跃的状态
这个变量称之为“标识”或者“信号”
'''
prompt = 'say something : '
active= True
while active :
    message = input(prompt)
    if message == 'quit':
        active = False
    else :
        print(message)