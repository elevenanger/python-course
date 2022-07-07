# @File  : test_name_function.py
# @Author: liuanglin
# @Time: 2022/6/20 22:17 
# -*- coding: utf-8 -*-

import unittest
from name_function import get_formatted_name

"""首先导入 unittest 以及需要测试的函数 get_formatted_name"""


class NameTestCase(unittest.TestCase):
    """
    定义测试类包含 'name_function.py' 测试用例
    测试类必须继承 unittest.TestCase 类
    """

    def test_first_name_last_name(self):
        """ 测试方法 eleven anger 是否生效"""
        formatted_name = get_formatted_name('eleven', 'anger')
        self.assertEqual(formatted_name, 'Eleven Anger')
        # self.assertEqual(formatted_name, 'Anger')
        """设置断言，判断函数执行的结果是否符合预期的结果"""

    """方法名必须以 test_ 开头，这样在运行 py 脚本时该方法将会自动执行"""

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('eleven', 'anger', "2nd")
        self.assertEqual(formatted_name, 'Eleven 2Nd Anger')


if __name__ == '__main__':
    """ 
    在函数执行时被赋值
    如果当前文件作为主函数运行
    __name__ 将会被赋值为 '__main__'
    这个情况下则调用 unittest.main()
    """
    unittest.main()
