# @File  : test_cities.py.py
# @Author: liuanglin
# @Time: 2022/6/27 20:43 
# -*- coding: utf-8 -*-
import unittest
from city_and_country import *


class CountryAndCityTestCase(unittest.TestCase):
    """city_and_country 模块测试类"""

    def test_country_and_city(self):
        format_name = form_country_and_city("china", "dongguan")
        self.assertEqual(format_name, "China, Dongguan")

    def test_with_population(self):
        format_str = form_with_population("china", "dongguan", 104_466_00)
        self.assertEqual(format_str, "China, Dongguan - population 10446600")

    if __name__ == '__main__':
        unittest.main()
