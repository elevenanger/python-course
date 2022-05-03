'''
@File    :   more_conditional_tests.py
@Time    :   2022/05/02 20:44:12
@Author  :   Liuanglin
@Desc    :   编写以下条件测试案例，输出结果
1、测试相等和不相等字符串
2、使用 lower() 方法进行测试
3、数字测试 == != > < >= <=
4、使用 and 和 or 关键字进行测试
5、判断一个元素是否在列表中
6、判断一个元素不在列表中
'''

canteen = ['egg','mushroom','chicken','banana']
celtics = [5,9,34,20]
print('egg'.lower == canteen[0].upper)
print('egg'.upper != canteen[0].lower)
print(1==celtics[1])
print(1!=celtics[1])
print(1>celtics[1])
print(1<celtics[1])
print(10>=celtics[1])
print(10<=celtics[1])
print('tomato' in canteen and 20 in celtics)
print('tomato' not in canteen or 20 in celtics)