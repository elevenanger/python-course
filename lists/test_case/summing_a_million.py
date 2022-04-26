'''
@File    :   summing_a_million.py
@Time    :   2022/04/24 21:15:15
@Author  :   Liuanglin
@Desc    :   创建一个 1，100万的列表
使用 min() max() 方法确定开始和终点位置
sum() 求和
'''


millions = range(1,1_000_001)
print(min(millions))
print(max(millions))
print(sum(millions))