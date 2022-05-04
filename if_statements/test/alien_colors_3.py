'''
@File    :   alien_colors_3.py
@Time    :   2022/05/03 10:56:05
@Author  :   Liuanglin
@Desc    :   基于 alien_colors_2 写一个 if-elif-else 链
1、如果是 green 获得 5 分
2、如果是 yellow 获得 10 分
3、如果是 red 获得 15 分 
'''


alien_colors = ['red','yellow','green']
for color in alien_colors :
    alien_color = color
    if alien_color == 'green' :
        print('you got 5 points')
    elif alien_color == 'yellow' :
        print('you got 10 points')
    elif alien_color == 'red' :
        print('you got 15 points')