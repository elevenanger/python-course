'''
@File    :   cubes.py
@Time    :   2022/04/24 21:24:47
@Author  :   Liuanglin
@Desc    :   cube-数字的三次方
创建一个 1，10 的 cube 列表
for 循环打印每个元素
'''

cubes = [value ** 3 for value in range(11)]
for cube in cubes :
    print(cube)

cubes = []
for number in range(11) :
    cubes.append(number ** 3)
    print(cubes[number])