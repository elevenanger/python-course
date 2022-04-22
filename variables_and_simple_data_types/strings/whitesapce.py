# 在代码中插入空白字符
# 空白字符以 \ 开头
line_breaker = "Python \n hehe" 
print(line_breaker)
tab_line = "Python\tpy"
print(tab_line)
python = "Python"
java = "Java"
# 可以在字符串中组合使用多个空白字符和变量
languages = f"Languages:\n\t{python}\n\t{java}"
print(languages)
word = "   word   "

# stripe() lstripe() rstripe() 方法一般用于清洗用户输入数据
# rstrip() 方法移除字符串右边多余的空格
print(f"...{word},{word.rstrip()}...")
# 上面只是临时移除字符串中右边多余的空格
print(f"...{word}...")
# 想要永久删除右边的空格，需要对变量重新赋值
word = word.rstrip()
print(f"...{word}...")
# 使用 lstripe() 方法移除左边的空格
print(f"...{word.lstrip()}...")
print(f"...{word}...")
# 调用 strip() 移除两边的空格
print(f"...{word.strip()}...")