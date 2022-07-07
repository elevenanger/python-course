'''
@File    :   return_value.py
@Time    :   2022/05/14 19:59:20
@Author  :   Liuanglin
@Desc    :   函数-返回值
'''

'''
定义函数的返回值
def func(args)
    function process
    return return_val
'''


def get_full_name(first_name, last_name):
    return (f"{first_name.title()} {last_name.title()}")


full = get_full_name('kevin', 'nance')
print(full)


def get_full_name(first_name, last_name, middle_name=''):
    if middle_name:
        return (f"{first_name.title()} {middle_name.title()} {last_name.title()}")
    else:
        return (f"{first_name.title()} {last_name.title()}")


print(get_full_name('michael', 'jordan'))
print(get_full_name('bruce', 'victor', 'k'))

'''
函数可以返回任意类型的数据
'''


def build_person(first_name, last_name, age='None'):
    person = {
        'first_name': {first_name},
        'last_name': {last_name},
    }
    if age:
        person['age'] = age
    return (person)


zhao = build_person('zhao', 'si', '30')
print(zhao)
