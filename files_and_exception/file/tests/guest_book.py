'''
@File    :   guest_book.py
@Time    :   2022/05/29 20:53:44
@Author  :   Liuanglin
@Desc    :   写一个 while 循环提示用户输入姓名
确保每次用户输入的信息追加到一个名为 guest_book.txt 的文件中
'''


file_name = 'guest_book.txt'
flag = True

with open(file_name,'a') as file_obj :
    while flag :
        name = input("What's your name : ")
        if name == 'quit' : break
        file_obj.write(f'{name}\n')