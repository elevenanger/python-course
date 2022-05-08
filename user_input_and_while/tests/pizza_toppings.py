'''
@File    :   pizza_toppings.py
@Time    :   2022/05/08 20:16:34
@Author  :   Liuanglin
@Desc    :   写一个循环
提示用户输入想要加在披萨上面的浇头
输入 quit 结束
告知用户已经添加的浇头并退出
'''

prompt = 'enter the toppings you want : '
toppings = []
flag = True
while flag :
    topping = input(prompt)
    if topping == 'quit' :
        print(toppings)
        flag = False
    else :
        toppings.append(topping)