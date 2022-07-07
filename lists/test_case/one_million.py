'''
@File    :   one_million.py
@Time    :   2022/04/24 21:08:48
@Author  :   Liuanglin
@Desc    :   创建一个 1 - 100_000_1 的列表并打印
为了简化，设置每次跳过 10 万数字
也可以按 Ctrl-c 退出程序运行
'''

millions = list(range(1, 1_000_002, 100_000))
for number in millions:
    print(number)
