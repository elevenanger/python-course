'''
@File    :   no_users.py
@Time    :   2022/05/03 14:36:26
@Author  :   Liuanglin
@Desc    :   使用 if 语句判断 hello_admin 的用户列表是否为空
1、为空则输出另外的信息
2、移除列表中的所有元素 确保输出正确的信息
'''


msg = 'have a nice day !'
special_msg = 'do you want to see some report?'
get_new_user_msg = 'we need some users.'
user_names = ['carl','kevin','kim','admin','howdy']
while user_names :
    removed_user = user_names.pop()
    if removed_user == 'admin' :
        print(f'{removed_user} , {special_msg}')
    else :
        print(f'{removed_user} , {msg}')
print(user_names)
if user_names :
    print('good')
else :
    print(get_new_user_msg)