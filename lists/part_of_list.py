'''
@File    :   part_of_list.py
@Time    :   2022/04/24 21:30:28
@Author  :   Liuanglin
@Desc    :   列表 - 对列表中的部分元素进行操作
'''

'''
1.切分列表
指定切分的起始位置索引和结束索引
切分后的子列表包括起始索引元素，不包括终止索引元素
list[first:last] -> list[first,last)
2.不指定起始索引，则默认从列表第一个元素开始
list[:last] -> list[0,last)
3.省略结束索引，从起始索引一直到最后一个元素
list[first:] -> list[first,end]
4.定义第三个参数，和range一样，在两个元素之间需要跳过的元素个数
'''
numbers = list(range(11))
print(numbers[2:5])
print(numbers[:3])
print(numbers[-2:])
print(numbers[2::3])

# 遍历子列表
for number in numbers[1:5]:
    print(number)

# 使用 new_list = from_list[:] 拷贝整个列表
new_numbers = numbers[:]
new_numbers.pop()
numbers.insert(1, 10)
print(f'{new_numbers},{numbers}')  # 打印列表，确认是两个独立的列表
