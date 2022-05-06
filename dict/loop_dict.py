'''
@Desc    :   遍历字典
'''

milk_way_station = {
    '1st' : 'Solar system',
    '2nd' : 'Cassiopeia'
}

'''
遍历dictionary
for k,v in dict.items() :
    do something with k
    do something with v
'''
for k,v in milk_way_station.items() :
    print(k)
    print(v)

'''
for k in dict.keys() :
    do something with k
or
for k in dict :
    do something with k
遍历字典中的 key
遍历 key 是遍历字典的默认行为
可以不用显式地写出 .keys() 方法
'''
for index in milk_way_station.keys() :
    print(index)

for index in milk_way_station :
    print(index)

zodiac_name = ['Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Ophiuchus','Sagittarius','Capricornus','Aquarius','Pisces']
zodiac = {}
for number in range(0,12) :
    index = number + 1
    if index == 1 :
        index = f'{index}st'
    elif index == 2 :
        index = f'{index}nd'
    elif index == 3 :
        index = f'{index}rd'
    else :
        index = f'{index}th'
    zodiac[index] = zodiac_name[number]
print(zodiac)

for index , name in zodiac.items() :
    print(f'{index} {name}')
    if name in zodiac_name :
        print(name)
# keys() 不仅仅是用于遍历，其实它返回了所有 key 的列表
if 'zode' not in zodiac.keys() :
    print('hehe')
# 使用 sorted(dict.keys()) 对 key 列表进行排序
for index in sorted(zodiac.keys()) :
    print (name)
# dict.values() 方法返回 value 列表
for value in zodiac.values() :
    print(value)

milk_way_station['3rd'] = 'Solar system'
print(milk_way_station)
# set() 方法是一种元素值唯一不重复的集合
distinct_station = set(milk_way_station.values())
print(distinct_station)
'''
定义集合
set = {e1,e2,...,en}
'''
stations = {'solar','else...'}
print(stations)