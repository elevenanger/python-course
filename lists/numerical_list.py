'''
@File    :   numerical_list.py
@Time    :   2022/04/24 20:40:21
@Author  :   Liuanglin
@Desc    :   列表-数字列表
'''

'''
1、range() 方法产生数字序列
range(start,end)  [start,end)
range(end) [0,end)
2、创建数字列表
list(range(args))
3、传入第三个参数，在指定范围中每次跳过多少数字
range(start,end,skip_number)
'''
from cgi import print_arguments


for number in range(1,5) :
    print(number)
for number in range(5) : 
    print(number)
# 使用 range() 创建数字列表
numbers = list(range(7))
for number in numbers : 
    print(number)
# range(arg1,arg2,args) arg3 指定步长
even_numbers = list(range(2,11,2))
for number in even_numbers :
    print(number)
squares = []
for number in range(11) :
    squares.append(number ** 2)
print(squares)

'''
数字列表中一些简单的统计方法
min(list) 最小的元素
max(list) 最大的元素
sum(list) 求和
'''
digits = list(range(11))
print(max(digits))
print(min(digits))
print(sum(digits))

'''
列表推导式
列表推导式将for循环、和创建新的元素整合到一行
并且自动添加每个元素到列表中
list = [element_value_expression for element_value in range(args)]
'''
squares = [value**2 for value in range(0,15,3)]
print(squares)

