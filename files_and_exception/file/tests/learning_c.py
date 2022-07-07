'''
@File    :   learning_c.py
@Time    :   2022/05/28 20:52:23
@Author  :   Liuanglin
@Desc    :   使用 replace() 方法可以替换字符串中的内容
读取 learning_python.txt 中每行的内容
将其中每行的 "Python" 替换为 "C"
'''

file_name = 'learning_python.txt'

with open(file_name) as file_obj:
    for line in file_obj:
        print(line.rstrip().replace('Python', 'C'))
