'''
@File    :   input.py
@Time    :   2022/05/08 18:16:38
@Author  :   Liuanglin
@Desc    :   input() 函数暂停程序 等待用户输入文本
一旦 Python 接收到了用户的输入
将输入赋值给变量进行程序逻辑的处理
'''

'''
variable = input(prompt)
input() 函数接收一个参数-提示或者指令
这是展示给用户的信息，提示用户需要做什么
用户输入的信息将被赋值给变量
对变量执行相应的操作
'''
msg = input('say something ... \n')
print(msg)

name = input("What's your name: ")
print(f'\n Hello,{name.title()}!')

# 提示语过长的情况可以将其拆分成多行赋值，这样使得代码更简洁
prompt = 'this is a very very very ....'
prompt += 'very long prompt '
print(input(prompt))

'''
input() 函数 Python 将用户输入的信息解释成 String
对于需要对用户录入的信息作为数字进行处理的情况
使用 int() 方法将其转换为数字
'''
age = input('How old are you ? ')
age = int(age)
if age >= 18:
    print(f"you are {age} years old, you can take it.")
else:
    print(f"young man")
