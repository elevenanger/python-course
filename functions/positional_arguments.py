'''
@File    :   positional_arguments.py
@Time    :   2022/05/11 21:00:29
@Author  :   Liuanglin
@Desc    :   位置参数
'''

'''
按顺序依次定义参数
def func(args)
Python 在函数定义中按参数名匹配参数
'''

def basketball_player(name,team) :
    print(f"{team.title()}'s {name.title() } ")

'''
重复调用函数
给参数进行赋值
'''
basketball_player('rondo','cetilcs')
basketball_player('kobe','lakers')
basketball_player('iverson','76er')
