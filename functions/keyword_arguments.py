'''
@File    :   keyword_arguments.py
@Time    :   2022/05/11 21:09:05
@Author  :   Liuanglin
@Desc    :   关键字参数是一组传递给函数的键值对
'''

def basketball_player(team,name) :
    print(f"{team.title()}'s {name.title() } ")

'''
调用函数的时候显式地给参数赋值
func(arg1=val1,...,argn=valn)
这样做可以确保赋值的准确性，不会因为顺序问题导致错误的赋值
'''
basketball_player(team='denver',name='anthony')

'''
在定义函数的时候可以为参数赋默认值
Python 会取调用函数的传值覆盖默认值
如果没有传值，则使用默认值
未赋默认值的参数需要在默认值参数之前定义
因为默认值使得该参数不需要在调用时赋值
Python 任然会按照顺序来给参数赋值
'''
def basketball_player(team,name='stein',league='NBA') :
    print(f"{name.title()} from {league.upper()}'s {team.title()}")

basketball_player('bulls','jordan')
basketball_player('guangdong','yi','CBA')