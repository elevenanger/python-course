'''
@File    :   pizza.py
@Time    :   2022/05/17 21:07:57
@Author  :   Liuanglin
@Desc    :   pizza 模块
'''


def make_pizza(size, *toppings):
    print(f'make {size} inch pizza : ')
    for topping in toppings:
        print(f'\t{topping}')
