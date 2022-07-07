'''
@File    :   continue_loop.py
@Time    :   2022/05/08 20:10:47
@Author  :   Liuanglin
@Desc    :   continue 语句跳出当前循环,回到循环逻辑的开始
'''

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number == 5:
        continue
    else:
        print(current_number)

for number in range(10):
    if number == 6:
        continue
    else:
        print(number)
