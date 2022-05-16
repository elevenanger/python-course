'''
@File    :   messages.py
@Time    :   2022/05/16 21:04:33
@Author  :   Liuanglin
@Desc    :   创建一个包含一系列信息的列表
将其作为参数传给 show_message() 函数
打印每一条信息
'''

messages = ['hello','darkness','my old friend']

def show_message(msgs) :
    for msg in msgs :
        print(msg.title())

show_message(messages)