'''
@File    :   printing_functions.py
@Time    :   2022/05/17 21:37:06
@Author  :   Liuanglin
@Desc    :   用于定义函数的文件
'''


def printing_function(*args):
    print('printing_functions.printing_function() :')
    for arg in args:
        print(f'\t{arg}')


def print_dict(**args):
    print('printing_functions.print_dict()')
    for k, v in args.items():
        print(f'\t{k.title()} {v.title()}')
