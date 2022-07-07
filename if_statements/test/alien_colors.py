'''
@File    :   alien_colors.py
@Time    :   2022/05/03 10:39:31
@Author  :   Liuanglin
@Desc    :   外星人射击游戏
一个外星人被击落，创建一个变量 alien_color 并赋值为 'green' 'red' 'yellow'
1、写一个语句测试颜色是否为 green 如果是，打印一条信息，玩家获得 5 分
2、编写该程序的一个版本通过 if 测试，另一个未通过 if  测试（未通过的不打印任何信息）
'''

alien_colors = ['red', 'yellow', 'green']
green_bonus = 5
dead_alien_color = 'green'
if dead_alien_color in alien_colors and dead_alien_color == alien_colors[-1]:
    print(f'you shut down a {dead_alien_color} alien, earned {green_bonus} points !')

if dead_alien_color != 'green':
    print('')  # do nothing
