'''
@File    :   guest.py
@Time    :   2022/05/29 20:49:59
@Author  :   Liuanglin
@Desc    :   提示用户输入姓名 将输入的内容写入文件中
'''

file_name = 'guest.txt'

with open(file_name,'w') as file_obj :
    name = input("What's your name : ")
    file_obj.write(f'{name}\n')