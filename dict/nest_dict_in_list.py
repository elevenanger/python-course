'''
@File    :   nest_dict_in_list.py
@Time    :   2022/05/07 21:20:23
@Author  :   Liuanglin
@Desc    :   嵌套-将字典作为列表的元素进行存储
'''

station_1 = {
    'name': 'Solar',
    'coordiantor_x': '11.33',
    'coordiantor_y': '45.33',
}

station_2 = {
    'name': 'Centaurus',
    'coordiantor_x': '14.43',
    'coordiantor_y': '25.29',
}

station_3 = {
    'name': 'Musca',
    'coordiantor_x': '23.43',
    'coordiantor_y': '90.29',
}

stations = [station_1, station_2, station_3]

for sta in stations:
    print(sta)

super_station = []
for number in range(20):
    super_station.append(station_1)
print(len(super_station))

for sta in super_station[:5]:
    if sta['name'] == 'Solar':
        sta['append'] = 'super'
        print(sta)
