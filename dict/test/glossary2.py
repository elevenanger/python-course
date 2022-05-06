'''
@File    :   glossary2.py
@Time    :   2022/05/06 21:59:13
@Author  :   Liuanglin
@Desc    :   使用字典存储 Python 的术语以及释义，并遍历字典
'''

terms = {
    'key' : '字典中的键',
    'value' : '字典中的值',
    'dict.items()' : '字典中元素的集合',
    'dict.keys()' : '字典键的列表',
    'dict.values()' : '字典值列表',
}

for term , meaning in terms.items() :
    print(f'{term} means {meaning}')