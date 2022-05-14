'''
@File    :   cities.py
@Time    :   2022/05/14 19:42:23
@Author  :   Liuanglin
@Desc    :   定义一个函数 describe_city() 
接收 城市名 和 国家名 参数
给国家参数一个默认值
调用函数
打印信息 城市在国家
分别输入三个城市的信息
至少有一个不在默认国家
'''

def describe_city(city_name,country='中国') :
    print(f"{country} - {city_name}")

describe_city('大理')
describe_city('长沙')
describe_city('西伯利亚','俄罗斯')