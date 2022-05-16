'''
@File    :   sandwiches.py
@Time    :   2022/05/16 21:54:27
@Author  :   Liuanglin
@Desc    :   定义一个包含多个元素的列表作为参数的函数
这些元素是顾客想要添加到三明治中的馅料
打印订购的三明治所有的馅料
调用函数三次
分别使用不同数量的馅料
'''

def make_sandwich(*stuffings) :
    print('----new order----')
    print(stuffings)
    for stuff in stuffings :
        print(f'\tadding stuffing : {stuff}')
    print('done!')

make_sandwich('drumstick','ham')
make_sandwich('ham','tomato','tuna')
make_sandwich('greens','turkey','pork','bacon')