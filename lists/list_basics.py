'''
@File    :   list_basics.py
@Time    :   2022/04/21 21:14:37
@Author  :   Liuanglin
@Desc    :   list 是特定顺序元素的集合
'''

# list 的格式 ['item','item']
animals = ['dog','cat','  frog  ','seal','whale']
print(animals)

'''
list 是顺序集合，可以通过索引访问特定的元素
获取元素： list[index] 
index 从 0 开始
可以像使用其它变量一样使用 list 中的任意一个元素
'''
print(f"{animals[0]},{animals[1].title()},{animals[2].strip()}")
# list 中可以存放任何数据
anything = ['puffy','vegetables','strawberry',10,3.14,False]
# 索引值为负数为倒序索引 -1 表示数组中的最后一个元素，-2 倒数第二个，以此类推
print(anything[-1])
print(anything[-2])