'''
@File    :   conditional_test.py
@Time    :   2022/05/02 20:29:28
@Author  :   Liuanglin
@Desc    :   一系列的条件测试案例
打印语句，描述各个测试案例并对每个测试案例进行预测
三个为 true ，三个 false
'''

zoo = ['seal', 'giraffe', 'tiger', 'lion']
print('is seal in zoo , I guess True')
print('seal' in zoo)
print('is zoo[2] == "tiger" , I guess true')
print(zoo[2] == 'tiger')
print('is lion in zoo , I guess true')
for animal in zoo:
    if animal == 'lion':
        print(animal == 'lion')

odds = [1, 3, 5, 7, 9]
print('2 is a odd , I guess False')
print(2 in odds)
print('8 is bigger than odd list last number, I guess False')
print(8 > odds[-1])
print('30 less than odd list sum , I guess False')
sum = 0
for number in odds:
    sum = sum + number
print(30 < sum)
