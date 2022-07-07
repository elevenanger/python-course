'''
@File    :   if_with_list.py
@Time    :   2022/05/03 14:22:11
@Author  :   Liuanglin
@Desc    :   条件语句组合列表一起使用
'''

zoo = ['giraffe', 'camel', 'tiger']
new_zoo = []
#  if list : 判断一个列表是否为空 列表至少存在一个元素 ： True 没有元素 False
if new_zoo:
    for animal in new_zoo:
        print(f'we got {animal}')
elif zoo:
    for animal in zoo:
        print(f'we got {animal}')
else:
    print('animal is on the way')
