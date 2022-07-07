'''
@File    :   buffet.py
@Time    :   2022/04/26 20:44:49
@Author  :   Liuanglin
@Desc    :   自助餐厅
想出五种基本的自助食品，使用元组存储它们
使用 for 循环遍历
尝试改变其中一个食品， Python 会报错
餐厅的菜单变化，替换了两种食物，对元组重新赋值，遍历新菜单
'''

food_menu = ('parrot', 'pizza', 'fish', 'meat', 'noodle')
for food in food_menu:
    print(f'our food : {food}')
# food[1] = 'chicken'
food_menu = ('chicken', 'potato', 'fish', 'meat', 'noodle')
for food in food_menu:
    print(f'our new food : {food}')
