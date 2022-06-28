# @File  : employee_class.py
# @Author: liuanglin
# @Time: 2022/6/28 21:41 
# -*- coding: utf-8 -*-

class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
        print(self.salary)
