'''
@File    :   glossary.py
@Time    :   2022/05/04 20:55:53
@Author  :   Liuanglin
@Desc    :   字典
1、五个编程术语做为 key ，存储他们的涵义做为 value
2、整齐打印输出名词和术语
'''

program_term = {
    'variable': '每个变量都关联一个值，它表示与变量相关的信息',
    'string': '字符串是一系列的字符',
    'list': '列表是按照特定顺序排列的元素的集合',
    'conditional_test': '条件测试是可以被判定为 True 或者 False 的表达式',
    'dictionary': '字典是一个或者多个键值对的集合，每个 key 都对应一个 value'
}

print(
    f"variable : {program_term.get('variable')}\nstring : {program_term['string']}\nlist : {program_term['list']}\nconditional test : {program_term['conditional_test']}\ndictionary : {program_term['dictionary']}")
