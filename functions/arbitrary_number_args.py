'''
@File    :   arbitrary_number_args.py
@Time    :   2022/05/16 21:14:39
@Author  :   Liuanglin
@Desc    :   传递任意数量的参数-可变参数列表
'''

'''
def func(*args) :
在函数参数定义前加上 * 表示该参数接收任意数量的参数
可以使用 for in 循环对参数进行遍历
'''


def make_pizza(*toppings):
    for topping in toppings:
        print(topping)


make_pizza('pepper', 'cheese')
make_pizza('tomato')
make_pizza('mushroom', 8)

'''
如果函数定义了多个入参
可变参数列表必须为最后一个参数
Python 首先匹配位置参数和关键字参数
然后将剩余的参数全部匹配为可变参数
'''


def make_pizza(size, *toppings):
    print(f'make {size} inch pizza : ')
    for topping in toppings:
        print(f'\t{topping}')


make_pizza(12, 'pepper', 'cheese')

'''
def func(**args) :
使用 **args 定义一个 dictionary 
可以自定义传入任意数量的键值对参数
'''


def person_info(first_name, last_name, **other_info):
    person = {'first': first_name.title(), 'last': last_name.title()}
    for k, v in other_info.items():
        person[k] = v.title()
    return person


einstein = person_info(first_name='albert', last_name='einstein', location='germany', race='jewish')
print(einstein)
