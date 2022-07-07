'''
@File    :   restaurant_seating.py
@Time    :   2022/05/08 18:58:21
@Author  :   Liuanglin
@Desc    :   询问用户有多少人共进晚餐
1、超过8位需要等位
2、不超8位就有位
'''

msg = 'how many peoples ?'
number = input(msg)
number = int(number)
if number > 8:
    print('you need to wait for a moment')
else:
    print('come with me')
