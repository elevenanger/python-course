'''
@File    :   three_restaurant.py
@Time    :   2022/05/18 21:24:17
@Author  :   Liuanglin
@Desc    :   使用 Restaurant 类
创建三个实例
并分别调用其中的方法
'''

from restaurant import Restaurant

shun_feng = Restaurant('shun feng', 'yue')
xiang_zhi_yuan = Restaurant('xiang zhi yuan', 'xiang')
xiao_si_chuan = Restaurant('xiao si chuan', 'chuan')

shun_feng.describe_restaurant()
xiang_zhi_yuan.describe_restaurant()
xiao_si_chuan.describe_restaurant()
