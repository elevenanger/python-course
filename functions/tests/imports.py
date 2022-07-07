'''
@File    :   imports.py
@Time    :   2022/05/17 21:46:25
@Author  :   Liuanglin
@Desc    :   使用各种 import 形式引入函数和模块
import module
import module as module_alias
from module import func
from module import func as func_alias
from module impot *
'''

import printing_functions
import printing_functions as pf
from another_module import func_a
from another_module import func_b
from printing_functions import *

func_a()
func_b()

printing_functions.print_dict(color='red', shape='pantagram')
pf.printing_function('charles', 'barkley')
printing_function('call function directly')
