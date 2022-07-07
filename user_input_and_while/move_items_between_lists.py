'''
@File    :   move_items_between_lists.py
@Time    :   2022/05/09 21:06:37
@Author  :   Liuanglin
@Desc    :   使用 while 在循环中操作列表中的元素
'''

unconfirmed_users = ['aliec', 'bob', 'carl', 'vince']
confirmed_users = []
# 将一个列表中的元素转移到另一个列表
while unconfirmed_users:
    confirmed_users.append(unconfirmed_users.pop())
print(f'confirmed {confirmed_users} , unconfirmed {unconfirmed_users}')

# 移除列表中的特定元素
passengers = ['mao', 'kang', 'thief', 'zhou', 'thief']
while 'thief' in passengers:
    passengers.remove('thief')
print(passengers)
