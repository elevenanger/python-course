'''
@File    :   functions_base.py
@Time    :   2022/05/11 20:37:11
@Author  :   Liuanglin
@Desc    :   函数-被命名的特定功能代码块
'''

'''
定义函数的语法
def func() :
    do something...

定义好的函数可以在程序别处使用
func()
'''


def greet_user():
    print("hello sir.")


# 调用函数
greet_user()

'''
定义需要传递参数的函数
def func(arg1,arg2,...,argn)

调用函数：
func(val1,val2,...,valn)
'''


def greet_user(name, age):
    print(f'hello {name.title()}')
    print(age)


greet_user('kevin', 22)
