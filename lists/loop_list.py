'''
@File    :   loop_list.py
@Time    :   2022/04/23 21:02:50
@Author  :   Liuanglin
@Desc    :   遍历列表
'''

'''
for in 遍历列表元素
for element in list :
    operate element
end 
'''
places = ['Wuyang', 'Xizang', 'Moscow', 'Hangzhou', 'Xinjiang']
count = 0;
for place in places:
    count = count + 1
    print(f'{count}.{place.title()}, nice place!')
# 无缩进代码则结束循环
print(count)
