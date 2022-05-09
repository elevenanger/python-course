'''
@File    :   deli_and_no_pastrami.py
@Time    :   2022/05/09 21:30:45
@Author  :   Liuanglin
@Desc    :   创建一个名为 sandwich_orders 列表
用不同的三明治名字填充它
创建一个空列表名为 finished_sandwichs
遍历订单列表 为每个订单打印信息
当每个三明治做完之后
将它移动到完成的三明治列表
全部移动完成后，打印完成的三明治
'''

sandwich_orders = ['tuna','ham','turkey']
finished_sandwiches = []

while sandwich_orders :
    cooking = sandwich_orders.pop()
    print(f'{cooking.title()} sandwich is making ...')
    finished_sandwiches.append(cooking)

print(f'Freshly baked sandwiches {finished_sandwiches}')

'''
使用上述的列表
确保 pastrami 三明治出现三次以上
打印信息 pastrami 三明治已经售罄
使用 while 循环将列表中的 pastrami 三明治全部移除
'''
for number in range(3) :
    finished_sandwiches.insert(number,'pastrami')
print(finished_sandwiches)

print('pastramies are sold out.')
while 'pastrami' in finished_sandwiches :
    finished_sandwiches.remove('pastrami')
print(finished_sandwiches)