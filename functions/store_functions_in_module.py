'''
@File    :   store_functions_in_module.py
@Time    :   2022/05/17 21:01:08
@Author  :   Liuanglin
@Desc    :   将函数放在一个独立的文件中，这个文件称之为模块
然后将模块 import 至程序中
'''

'''
import module 
整个导入模块
'''
import pizza
'''
可以为模块设置别名
更方便的调用模块中的函数
import module as module_alias
'''
import pizza as pz
'''
导入指定的函数
from module import func1(),func2(),...
'''
from person import person_info,describe_person
'''
如果需要导入的函数和已有的函数名冲突
或者函数名较长
可以为函数设置一个别名
在当前文件中使用该别名调用此函数
from module import func() as func_alias()
'''
from person import describe_person as dp

'''
使用 * 号导入模块中的所有函数
from module import *
'''
from pizza import *

# 调用模块中的函数 module.func()
pizza.make_pizza(12,'pepper','ham')
pizza.make_pizza(14,'mushroom','cheese','ham')

# 直接调用导入的函数
mao = person_info(first_name='mao',last_name='run',title='Taizu')
describe_person(mao)
# 通过别名调用函数
dp(mao)

# 使用模块别名调用模块中的函数
pz.make_pizza(16,'red pepper')

# 导入了 pizza 模块全部函数，直接使用函数名进行调用
make_pizza(10,'turkey')