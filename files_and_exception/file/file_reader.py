'''
@File    :   file_reader.py
@Time    :   2022/05/28 19:50:05
@Author  :   Liuanglin
@Desc    :   读取文件信息
'''

'''
open('file') 
open() 以文件名作为参数
Python 在程序当前执行目录查到匹配的文件
open() 方法返回表示文件的对象
as file_input 将文件对象赋值给 file_input
with 在文件访问不再被使用时关闭文件资源
read() 方法读取文件中的内容将其存储为字符串并赋值给 contents
rstrip() 方法去除右侧所有的空格
'''
with open('pi_digest.txt') as file_input:
    contents = file_input.read()
    print(contents.rstrip())

'''
with open(file_name) as file_obj :
    for line in file_obj :
        print(line)
逐行读取文件
'''
with open('pi_digest.txt') as file_input:
    for line in file_input:
        print(f'lines {line.rstrip()}')

'''
with open(file_name) as file_obj :
    lines_list = file_obj.read_lines()
将文件中的行信息转换为 list
'''
with open('pi_digest.txt') as file_input:
    lines_list = file_input.readlines()
print(lines_list)

'''
操作文件内容
'''
with open('pi_digest.txt') as file_input:
    lines = file_input.readlines()
    line_str = ''
    for line in lines:
        line_str += line.strip()
    print(line_str)
    # 字符串都是字符列表
    print(f"{line_str[:10]}...")
    # str in str 判断是否存在包含关系
    print('3.14' in line_str)
