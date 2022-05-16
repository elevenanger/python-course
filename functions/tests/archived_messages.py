'''
@File    :   archived_messages.py
@Time    :   2022/05/16 21:11:40
@Author  :   Liuanglin
@Desc    :   基于 sending_messages.py
使用消息列表的拷贝调用 send_messages()
'''


messages = ['hello','darkness','my old friend']
sent_messages = []

def send_messages(msgs) :
    while msgs :
        msg = msgs.pop()
        print(msg)
        sent_messages.append(msg)

send_messages(messages[:])

print(messages)
print(sent_messages)