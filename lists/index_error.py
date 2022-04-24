'''
@File    :   index_error.py
@Time    :   2022/04/23 20:53:58
@Author  :   Liuanglin
Desc     :   列表错误一般发生在操作不存在的元素
'''


recipe = ['dumpling','tomato','noodle','rice','egg','tuna']
recipe.remove('pie')
print(recipe[6])
print(recipe[2])