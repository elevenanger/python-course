'''
@File    :   movie_tickets.py
@Time    :   2022/05/08 20:25:16
@Author  :   Liuanglin
@Desc    :   电影院影票根据顾客的年龄收费
1、小于 3 岁 免费
2、3~12岁 10 元
3、12 岁以上 15 元
'''

prompt = 'how old are you : '
while True:
    price = 15
    msg = input(prompt)
    if msg == 'quit':
        print('see you ')
        break
    age = int(msg)
    if age <= 0 and age > 150:
        print('You are miracle')
        break
    elif age > 0 and age < 3:
        price = 0
    elif age >= 3 and age <= 12:
        price = 10
    print(f"you need to pay {price} for the ticket ")
