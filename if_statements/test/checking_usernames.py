'''
@File    :   checking_usernames.py
@Time    :   2022/05/03 14:51:12
@Author  :   Liuanglin
@Desc    :   用户名检查规则
1、创建5个用户名列表 current_users
2、创建另外5个用户名列表 new_users 确保其和用户名列表中存在2个重合的元素
3、遍历 new_users ,检查是否已被占用，有则提示他换一个新的用户名，没有则提示可用
4、比较规则大小写敏感 为此额外创建2个新的列表 确保其中的字母都是小写以及大写
'''

current_user = ['James', 'Bond', 'RAT', 'cloud', 'brondy']
new_users = ['McHale', 'Stein', 'Jones', 'BOND', 'rat']
current_user_upper = []
current_user_lower = []

while current_user:
    user = current_user.pop()
    current_user_lower.append(user.lower())
    current_user_upper.append(user.upper())

print(current_user_lower)
print(current_user_upper)
for user_name in new_users:
    if user_name in current_user or user_name in current_user_lower or user_name in current_user_upper:
        print(f'sorry , {user_name} are taken by someone.')
    else:
        print(f'{user_name} is avalable.')
