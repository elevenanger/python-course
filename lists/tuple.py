'''
@File    :   tuple.py
@Time    :   2022/04/26 20:30:57
@Author  :   Liuanglin
@Desc    :   元组
元组是 Python 中另一种重要的序列结构
和列表类似
元组也是由一系列按照特定顺序排序的元素组成
元组和列表的不同之处：
列表的元素是可变的，而元组一旦被创建，它的元素就不可变更
通常，元组用于保存无需修改的内容
'''

'''
定义元组: tuple = (val1,val2)
获取元素 elementVal = tuple[index]
'''
ori_tuple = (10,20)
print(ori_tuple[0])
print(ori_tuple[-1])
# 如果定义只有一个元素的元组，也需要在唯一一个元素后面带上 ,
one_element_tuple = (1,)
print(one_element_tuple[0])
# 遍历元组的方式也和遍历 list 的方法一样
for ele in ori_tuple :
    print(f'ori_tuple element value : {ele}')
ori_tuple = (100,200)
# 元组中的元素不能变,但是元组可以重新赋值
# 如果想要变更元组，需要重新定义整个元组
for ele in ori_tuple :
    print(f'changed tuple element value : {ele}' )