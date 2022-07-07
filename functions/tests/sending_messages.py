'''
@File    :   sending_messages.py
@Time    :   2022/05/16 21:07:27
@Author  :   Liuanglin
@Desc    :   基于 messages.py
定义一个 send_messages() 函数
打印每条信息
并将信息转移到 sent_message 列表
'''

messages = ['hello', 'darkness', 'my old friend']
sent_messages = []


def send_messages(msgs):
    while msgs:
        msg = msgs.pop()
        print(msg)
        sent_messages.append(msg)


send_messages(messages)

print(messages)
print(sent_messages)
