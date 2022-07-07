'''
@File    :   modify_elements.py
@Time    :   2022/04/22 19:32:30
@Author  :   Liuanglin
@Desc    :   修改列表
'''

animals = ['rat', 'rabbit', 'tiger', 'chicken', 'cow', 'bull']
print(animals)
# 修改列表中的元素 list[index] = newVal
animals[1] = 'pig'
animals[-1] = 'seal'
print(animals)

# 往列表末尾新增元素 list.append(new_element)
animals.append('monkey')
print(animals)

# 创建一个空列表，使用 append 方法往列表中追加元素
initial_zoo = []
initial_zoo.append('panda')
initial_zoo.append('snake')
initial_zoo.append('buffalo')
print(initial_zoo)

'''
append 方法可以追加任意元素，包括 list
在 list 中追加的是对象的引用
修改 animals 之后， initial_zoo 也会随之变化
'''
initial_zoo.append(animals)
print(initial_zoo)
print(initial_zoo[-1][0])
animals.append('dinasour')
print(initial_zoo)
print(initial_zoo[-1][-1])

'''
insert 方法往数组中插入元素
list.insert(index,element) 
index >= 0 : 在 list[index] 之后插入元素
index < 0 在 list[index] 之前插入元素
'''
new_zoo = initial_zoo;
print(new_zoo)
new_zoo.insert(0, 'fenix')
new_zoo.insert(-1, 'dragon')
print(new_zoo)
print(initial_zoo)

'''
del 方法删除数组中的元素
del list[index]
'''
del initial_zoo[0]
print(initial_zoo)
del initial_zoo[-1]
print(initial_zoo)

'''
pop 方法取出数组中最后一个元素
可以在取出其之后使用该元素
'''
escaped_animal = initial_zoo.pop()
# 可以使用该元素进行后续的操作
print(escaped_animal)
# 该元素已从 list 中移除
print(initial_zoo)

'''
pop 方法还可以移除指定位置的元素
list.pop(index)
'''
print(initial_zoo.pop(0))
print(initial_zoo)

'''
remove() 方法移除 list 中的元素
list.remove(element_value)
'''
initial_zoo.remove('snake')
print(initial_zoo)
'''
使用变量的值匹配需要移除的元素
匹配的是变量的值
remove() 只移除 list 中第一个匹配的元素
'''
die_in_peace = 'buffalo'
print(die_in_peace)
middle_one = 'mouse'
initial_zoo.append(middle_one)
initial_zoo.append(die_in_peace)
print(initial_zoo)
initial_zoo.remove(die_in_peace)
print(initial_zoo)
