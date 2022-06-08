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
alien_0['tmp_station'] = 'moon'
print(alien_0)
# del dict[key] 通过 key 从字典中删除一个键值对
del alien_0['tmp_station']
print(alien_0)
'''
字典中的键值对较多的时候，使用合适的格式化的写法使得可读性变得更强
dict = {
    key1 : val1,
    key2 : val2,
}
在每行键值对的最后用一个逗号 , 方便后续添加元素
'''
solar_stations = {
    '1st': 'Moon',
    '2nd': 'Pluto',
    '3rd': 'Mercury',
}
print(solar_stations['3rd'].upper())
'''
使用 dict[key] 当 key 不存在的时候，程序会报错
用 dict.get(key,optional_val) 方法可以更安全地获取元素
optional_val 是可选传参，当key对应的value不存在时返回 optional_val
未定义 optional_val 而且 key 对应的元素不存在时，会返回 None
这并非一个错误的信息，而是一个特殊的值，表示 值不存在
'''
second_station = solar_stations.get('2nd')
print(second_station)
fourth_station_with_notice = solar_stations.get('4th','solar 4th station is building ... ')
print(fourth_station_with_notice)
fourth_station = solar_stations.get('4th')
print(fourth_station)