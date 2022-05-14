'''
@File    :   t_shirt.py
@Time    :   2022/05/14 19:29:19
@Author  :   Liuanglin
@Desc    :   定义一个名为 make_shir() 的函数
函数参数为尺码和需要印在T恤上的文字
分别使用位置参数和关键字参数调用函数
'''

def make_shirt(size,text) :
    print(f"new shirt \n \tsize : {size.upper()} \n\ttext : {text.title()}")

make_shirt('m','world peace')
make_shirt(size='L',text='super man')

'''
修改 make_shirt() 函数
默认尺码为 L 
默认文字为 I love Python
分别制作 L 和 M 码 T恤 使用默认的文字
制作一件任意尺码的T恤 使用其它的文字
'''
def make_shirt(size = 'L',text='I love Python') :
    print(f"new shirt \n \tsize : {size.upper()} \n\ttext : {text.title()}")
    
make_shirt()
make_shirt('m')
make_shirt('s','love & peace')