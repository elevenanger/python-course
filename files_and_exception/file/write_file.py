'''
@File    :   write_file.py
@Time    :   2022/05/29 20:29:01
@Author  :   Liuanglin
@Desc    :   写文件
'''

file_name = 'write_something.txt'

'''
with open(file_name,'w') as file_obj :
    file_obj.write('information')
往文件中写数据
open() 第一个参数是需要打开的文件名
第二个参数 'w' 表示以写权限打开文件
可以使用 r 读模式
w 写模式
a 附加模式
r+ 读写权限
第二个参数不赋值则默认为只读权限
当你试图写入的文件不存在时 open() 函数会自动创建文件
但是需要注意的是 w 模式打开一个已有的文件时会将文件中的内容清空
对 file_obj 方法使用 write() 方法将字符串写入文件中
'''
with open(file_name, 'w') as file_obj:
    file_obj.write('say something ...')

'''
新的 open() w 模式打开已有文件会覆盖文件已有的内容
在同一个 open() w 模式下
多次使用 write() 函数将不断追加内容
write() 方法往文件末尾追加字符串
需要在程序中进行换行处理
'''
with open(file_name, 'w') as file_obj:
    file_obj.write('say something else ...\n')
    file_obj.write('say something else again ... \n')

'''
使用 open() 方法 a append 模式往文件中追加内容二不会清空文件中已有的数据
如果文件不存在
Python 也会自动创建文件
'''
with open(file_name, 'a') as file_obj:
    file_obj.write('append something ... \n')
