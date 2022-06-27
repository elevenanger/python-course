# @File  : city_and_country.py
# @Author: liuanglin
# @Time: 2022/6/27 20:39 
# -*- coding: utf-8 -*-

"""
写一个函数接收两个参数 city 和 country
函数返回一个格式化后的字符串
格式为 ： Country, City
将函数存储到一个模块中
创建一个名为 test_cities.py 的测试文件测试上面定义的函数
"""


def form_country_and_city(country_name, city_name):
    return f"{country_name.title()}, {city_name.title()}"


def form_with_population(country_name, city_name, population):
    """新增 population 人口参数"""
    format_name = form_country_and_city(country_name, city_name)
    return f"{format_name} - population {population}"
