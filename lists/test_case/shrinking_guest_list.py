'''
@File    :   shrinking_guest_list.py
@Time    :   2022/04/22 21:08:18
@Author  :   Liuanglin
@Desc    :   由于疫情的原因，桌子无法按时送达，只剩下两个席位
基于 more_guest 最终的宾客列表，打印信息说明只有两个席位
使用 pop() 方法移除到只剩下两位宾客，向每位移除的宾客致歉
告知剩下的两位宾客他们的邀请任然有效
使用 del 方法删除仅剩的两位宾客，并打印最终的空列表
'''

guests = ['liu', 'mao', 'xi', 'qin', 'li', 'gao']
print("We only have two seats for dinner .")
apology = 'Sorry sir.'
print(f'{guests.pop().title()} {apology}')
print(f'{guests.pop().title()} {apology}')
print(f'{guests.pop().title()} {apology}')
print(f'{guests.pop().title()} {apology}')
greetings = 'you are lucky'
print(f'{guests[0].title()},{greetings}')
print(f'{guests[1].title()},{greetings}')
del guests[0]
del guests[0]
print(guests)