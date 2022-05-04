'''
@File    :   hello_admin.py
@Time    :   2022/05/03 14:30:26
@Author  :   Liuanglin
@Desc    :   五个用户名列表，包括 admin 
遍历列表，对每个用户发送一句问候
1、用户名为 admin 特殊语句
2、其它的用户 普通语句
'''

msg = 'have a nice day !'
special_msg = 'do you want to see some report?'
user_names = ['carl','kevin','kim','admin','howdy']
for user_name in user_names :
    if user_name == 'admin' :
        print(f'{user_name} , {special_msg}')
    else :
        print(f'{user_name} , {msg}')