'''
@File    :   pizzas.py
@Time    :   2022/04/23 21:35:32
@Author  :   Liuanglin
@Desc    :   三种最喜欢的披萨，使用 for-in 遍历披萨列表
'''

pizzas = ['black peper','orleans chicken','seafood']
msg = 'I love'
for pizza in pizzas : 
    print(f'{msg} {pizza.title()} pizza')
print('really dilicious !'.title())