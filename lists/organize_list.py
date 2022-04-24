'''
@File    :   organize_list.py
@Time    :   2022/04/23 19:30:42
@Author  :   Liuanglin
@Desc    :   对列表中的元素进行排序   
'''

'''
使用 list.sort() 方法永久改变列表中元素的顺序
默认顺序排序
对于字符串，使用的是字典序
数字按大小排序
'''
recipe = ['dumpling','tomato','noodle','rice','egg','tuna']
recipe.sort()
print(recipe)
price = [6.2,12,13,15,2,1,35]
price.sort()
print(price)
# list.sort(reverse=True) sort 方法传入 reverse=True 对列表元素进行序排序
recipe.sort(reverse=True)
print(recipe)
price.sort(reverse=True)
print(price)

# sorted(list) 临时改变列表元素的顺序,顺序排序,不改变列表
recipe = ['dumpling','tomato','noodle','rice','egg','tuna']
print(sorted(recipe))
# 也可以传入 reverse=True 倒序排序
print(sorted(recipe,reverse=True)) 
print(recipe)
# list.reverse() 方法对列表进行年代序倒序排序,年代序是列表自然索引顺序，不是字典序
new_food = 'chicken'
recipe.insert(2,new_food)
print(recipe)
recipe.reverse()
print(recipe)
# 再次调用 reverse 方法恢复列表原本的顺序
recipe.reverse()
print(recipe)
# len(list) 返回列表元素个数
print(len(recipe))
empty = []
print(len(empty))