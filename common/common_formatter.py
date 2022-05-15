'''
@File    :   common_formatter.py
@Time    :   2022/05/15 20:34:44
@Author  :   Liuanglin
@Desc    :   公共的格式化函数
'''


def format_index(index) :
    if(index == 1) : return f'1st'
    if(index == 2) : return f'2nd'
    if(index == 3) : return f'3rd'
    return f'{index}th'