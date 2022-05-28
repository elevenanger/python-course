'''
@File    :   read_from_path.py
@Time    :   2022/05/28 20:02:40
@Author  :   Liuanglin
@Desc    :   从文件路径读取文件
'''

'''
从相对路径读取文件
with open('file_path/filename') as file_obj :
'''
relative_path = 'files_path/'
with open(f'{relative_path}content.txt') as relative_input :
    content = relative_input.read()
    print(content.title())

'''
从决定路径读取文件信息
'''
absolute_path = '/Users/liuanglin/Projects/python-course/files_and_exception/file/files_path/'
with open(f'{absolute_path}content.txt') as absolute_input :
    abs_content = absolute_input.read()
    print(f'absolute {abs_content.title()}')