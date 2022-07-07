from email import header

'''
@File    :   guest_list.py
@Time    :   2022/04/22 20:35:19
@Author  :   Liuanglin
@Desc    :   创建一个列表，包括三个你想邀请共进晚餐的人，并发出邀请
'''

emperors = ['mao', 'qin', 'li']
dates = ['today', 'tomorror', 'day after tomorror']
invite_message = 'Sir , may you have dinner with me'
print(f'{emperors[0].title()} {invite_message} {dates[0]} ?')
print(f'{emperors[1].title()} {invite_message} {dates[1]} ?')
print(f'{emperors[2].title()} {invite_message} {dates[2]} ?')
