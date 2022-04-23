'''
@File    :   more_guests.py
@Time    :   2022/04/22 20:54:59
@Author  :   Liuanglin
@Desc    :   基于guest_list,现在有了更大的餐桌，再多邀请三个人前来参加晚宴
使用 insert() 在列表开头插入新的人名
使用 insert() 在列表中检插入新的人名
使用 append() 在列表末尾插入新的人名
使用一个新的信息列表，为每个人发出不同的邀请
'''

emperors = ['mao','qin','li']
emperors.append('gao')
emperors.insert(0,'liu')
emperors.insert(2,'xi')
new_msg = 'Sir , come to my dinner today.'
guest_order = [1,2,3,4,5,6]
print(f'{guest_order[0]}.{emperors[0].title()} {new_msg}')
print(f'{guest_order[1]}.{emperors[1].title()} {new_msg}')
print(f'{guest_order[2]}.{emperors[2].title()} {new_msg}')
print(f'{guest_order[3]}.{emperors[3].title()} {new_msg}')
print(f'{guest_order[4]}.{emperors[4].title()} {new_msg}')
print(f'{guest_order[5]}.{emperors[5].title()} {new_msg}')
print(emperors)