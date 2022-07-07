from email import message
from turtle import title

first_name = "anger"
last_name = "liu"
# 在字符串中插入变量
# f 表示 format ，用 f 格式化的字符串叫做 f-字符串
# python 格式化变量值为 String 的格式 f"{varialble}"
full_name = f"{first_name} {last_name}"
print(full_name)
# 可以在 f 字符串使用任意字符串拼接变量
# full_name.title() 将变量调用title() 方法的值转换成字符串进行拼接
print(f"Hello,{full_name.title()} !")
# 将 f 字符串赋值给变量
message = f"this is a message".title(), {full_name}
print(message)
