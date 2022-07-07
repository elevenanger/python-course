'''
@File    :   exception_base.py
@Time    :   2022/06/01 21:39:13
@Author  :   Liuanglin
@Desc    :   异常的基础信息   
'''

'''
print(5/0) 
Traceback (most recent call last):
  File "/Users/liuanglin/Projects/python-course/exceptions/exception_base.py", line 8, in <module>
    print(5/0)
ZeroDivisionError: division by zero
Traceback 输出错误信息
ZeroDivisionError 是一个异常对象
Python 创建这种对象用于响应无法处理的请求
当这种情况发生 
Python 终止程序并告诉我们引发的异常类型
当你察觉某种异常可能发生
可以通过 try-except 块来处理可能发生的异常
告诉 Python try 运行某一段代码
并告诉 Python 当某种特定的异常发生时应该怎么做
try :
    do something(try block)
except ExceptionObject :
    do something to handle it(except block)
首先执行 try 代码块中的代码
如果正常执行则跳过 except 块的代码
如果发生异常
Python 查找可以与异常信息相匹配的 except 块
执行对应 except 块中的代码并继续执行后面的代码，程序不会中断
'''
try:
    print(5 / 0)
except ZeroDivisionError:
    print('0不能作为除数')

print('输入两个数字，输出他们的商。')
print('输入 q 退出程序')
while True:
    first_number = input('\n 第 1 个数字 ： ')
    if first_number == 'q':
        break
    second_number = input('\n 第 2 个数字 ： ')
    if second_number == 'q':
        break
    # 将可能出现异常的代码使用 try-except 包裹
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('0不能作为除数')
    else:
        print(answer)

file_name = 'exception_base.py'
try:
    with open(file_name, encoding='utf-8') as file_obj:
        content = file_obj.read()
except FileNotFoundError:
    print(f"{file_name} 文件不存在")
else:
    words = content.split()
    num_words = len(words)
    print(f"the file {file_name} has {num_words} words")
