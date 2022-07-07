'''
@File    :   nest_list_in_dict.py
@Time    :   2022/05/08 16:48:30
@Author  :   Liuanglin
@Desc    :   将列表嵌套在字典中
'''

# 银河铁道

zodiac = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Ophiuchus', 'Sagittarius',
          'Capricornus', 'Aquarius', 'Pisces']
milky_railway = {
    'galaxy': 'Milky Way',
    'stations': zodiac,
}

for constellation in milky_railway['stations']:
    print(constellation)
