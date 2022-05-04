'''
@File    :   alien_colors_2.py
@Time    :   2022/05/03 10:47:31
@Author  :   Liuanglin
@Desc    :   选择 alien_color 中的一个颜色，写一个 if-else 链
1、如果外星人颜色为 green ,打印玩家获得5分
2、如果不是 green 打印获得 10 分
3、一个版本是 if 条件判断，另一个版本通过 else 条件判断
'''


alien_colors = ['red','yellow','green']
green_points = 5
other_points = 10
for color in alien_colors :
    dead_alien_color = color
    if dead_alien_color == 'green' :
        print(f'you got {green_points}!')
    else :
        print(f'you got {other_points}!')
        
for color in alien_colors :
    dead_alien_color = color
    if dead_alien_color != 'green' :
        print(f'you got {other_points}!')
    else :
        print(f'you got {green_points}!')