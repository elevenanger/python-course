'''
@File    :   my_pizzas.py
@Time    :   2022/04/24 22:02:01
@Author  :   Liuanglin
@Desc    :   披萨列表
1、从源列表创建一个新列表
2、为每个列表添加一个不同的元素
3、遍历列表，确保是独立的两个列表
'''

pizzas = ['black peper', 'orleans chicken', 'seafood']
new_pizzas = pizzas[:]
pizzas.append('tomato')
new_pizzas.append('potato')
for pizza in pizzas:
    print(f'pizza: {pizza}')
for pizza in new_pizzas:
    print(f'new_pizza: {pizza}')
