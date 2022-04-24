'''
@File    :   seeing_in_the_world.py
@Time    :   2022/04/23 20:10:06
@Author  :   Liuanglin
@Desc    :   五个最想去的地方
将五个地方存放在一个列表中，确保它不是字典序的
打印原始列表
使用 sorted() 方法将列表按照字典序打印，不改变原始列表
打印列表，确保其未被改变
使用 sorted() 方法按照逆字典序打印列表，不改变原始列表
打印列表，确保其未被改变
reverse() 翻转列表，打印列表
再次使用 reverse() 翻转列表，打印列表
使用 sort() 方法按字典序对列表排序，打印列表
使用 sort() 方法逆字典序对列表排序，打印列表
'''

places = ['Wuyang','Xizang','Moscow','Hangzhou','Xinjiang']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print(len(places))