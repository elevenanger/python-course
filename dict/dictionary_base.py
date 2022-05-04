'''
@File    :   dictionary_base.py
@Time    :   2022/05/03 19:57:42
@Author  :   Liuanglin
@Desc    :   字典
'''

'''
字典-Python的一种键值对数据结构
键值对是一种互相关联的数据
每一个 key 都对应一个 value
在 Python 中可以创建的任何对象都可以作为字典中的 value 
dict = {key_1:value_1,key_2:value_2,...,key_n:value_n}
从字典中获取某个 key 的值
value = dict[key]
'''
alien_0 = {'color':'green','points':5}
print(alien_0)
print(alien_0['color'])
'''
字典是动态的数据结构
可以在任意时候往字典中动态的添加新的键值对
dict[key]=value
从 Python 3.7 开始，字典会保留其定义的顺序
当 print(dict) 或者遍历字典
会按照元素添加的顺序进行输出
'''
alien_0['galaxy'] = 'Abadango'
print(alien_0)
'''
dict = {} 使用空的大括号定义一个空的字典
存储用户提供的数据或者
程序逻辑自动产生大量键值对数据的情况下
使用空字典
''' 
alien_0 = {}
print(alien_0)
alien_0['galaxy'] = 'Abadango'
print(alien_0)
'''
dict[exist_key] = new_val
修改字典中已有key的值
'''
alien_0['galaxy'] = 'Milky Way'
print(alien_0)
