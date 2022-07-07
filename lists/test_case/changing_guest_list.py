'''
@File    :   changing_guest_list.py
@Time    :   2022/04/22 20:40:11
@Author  :   Liuanglin
@Desc    :   宾客列表中的一位没空，你需要换一个人邀请

基于 guest_list ，打印不能参与的人名
将列表中没空的人名替换成新邀请的人名
向仍然在你列表中发出新的邀请信息
'''

emperors = ['mao', 'qin', 'li']
busy_man = emperors.pop()
print(busy_man.title())
new_man = 'wang'
emperors.append(new_man)
new_message = "Sir , our dinner sill be fine , I'm waiting for you coming."
print(f'{emperors[0].title()} {new_message}')
print(f'{emperors[1].title()} {new_message}')
print(f'{emperors[2].title()} {new_message}')
