'''
@File    :   learning_python.py
@Time    :   2022/05/28 20:36:46
@Author  :   Liuanglin
@Desc    :   创建一个文件
在文件中输入几行总结从 Python 中学到的知识
每一行以 In Python you can 开头
将文件命名为 learning_python.txt 与程序保存在同一个目录下
读取文件中心信息打印三次：
1、read() 文件对象打印
2、使用 for 循环遍历
3、将文件中的行存储在 list 中，遍历 list 打印
'''


file_name = 'learning_python.txt'

with open(file_name) as file_obj :
    print(file_obj.read())

with open(file_name) as file_obj :
    for line in file_obj :
        print(f"lines {line.rstrip()}")
        
with open(file_name) as file_obj :
    lines = file_obj.readlines()
    for line in lines :
        print(f"lines list {line.rstrip()}")