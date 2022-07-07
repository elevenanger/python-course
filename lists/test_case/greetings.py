'''
@File    :   greetings.py
@Time    :   2022/04/21 21:38:21
@Author  :   Liuanglin
@Desc    :   
使用 names.py 中的数组元素
对其中每一个人问好
问好的信息是相同的
'''

from names import names

message = 'hello,'.title()

print(f"{message}{names[0]}")
print(f"{message}{names[1]}")
print(f"{message}{names[-2]}")
print(f"{message}{names[-1]}")
