'''
@File    :   passing_list.py
@Time    :   2022/05/16 20:40:59
@Author  :   Liuanglin
@Desc    :   将 list 作为参数传入函数
'''


def greet_users(names):
    for name in names:
        print(f'hello {name.title()}')


usernames = ['carl', 'steve']
greet_users(names=usernames)

'''
可以在函数中对传入的参数进行修改
这些变更将会永久有效
'''
unchecked_users = ['carl', 'kevin', 'carter', 'williams']
checked_users = []


def check_user(users):
    while users:
        checked_users.append(users.pop())


check_user(unchecked_users)
print(unchecked_users)
print(checked_users)

'''
如果想要不修改原 list
可以将原 list 的拷贝作为参数传入函数
除非必要 尽量避免这种使用方式
因为拷贝列表需要额外的存储空间和计算资源
尤其是对于大量数据的列表进行拷贝操作
'''
unchecked_users = ['carl', 'kevin', 'carter', 'williams']
checked_users = []
check_user(unchecked_users[:])
print(unchecked_users)
print(checked_users)
