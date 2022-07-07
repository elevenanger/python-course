'''
@File    :   user_profile.py
@Time    :   2022/05/16 22:02:55
@Author  :   Liuanglin
@Desc    :   定义函数 build_profile()
使用姓、名和任意三个其它的特征描述一个人
'''


def build_profile(first, last, **characteristics):
    person = {}
    person['first'] = first.title()
    person['last'] = last.title()
    for k, v in characteristics.items():
        person[k] = v.title()
    return person


yao = build_profile('yao', 'ming', occupation='basketball player', address='shang hai', team='huston rockets')
print(yao)
