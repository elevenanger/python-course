'''
@File    :   dog.py
@Time    :   2022/05/18 20:38:01
@Author  :   Liuanglin
@Desc    :   使用类对狗狗进行建模
'''

'''
class ClassName :
使用 class 定义类
类名首字母大写
'''
class Dog:
    
    '''
    在类中所有的函数都称之为方法
    方法和函数的定义基本一致
    只是调用方式上有所区别
    __init__() 方法比较特殊
    每当创建这个类的对象时
    都会自动调用该方法
    self 参数在 __init__() 方法是必须的
    而且必须是第一个参数
    在 Python 后续调用此方法创建该类的实例时
    方法调用会自动传递 self 参数
    每个与实例相关的方法都会自动传递 self 参数
    self 参数是对于该实例的引用
    它使得单个实例可以访问类中的属性和方法
    当创建新的实例对象
    只需要传递 name 和 age 作为参数
    self 会自动传递，不需要显式地给此参数赋值
    
    '''
    def __init__(self,name,age) :
        '''
        name 和 age 变量都有一个前缀 self.
        每个拥有 self. 前缀的变量对于类中的所有方法都是可用的
        可以从该类所有实例访问这两个变量
        这种可以通过实例访问的变量称之为 属性
        '''
        self.name = name
        self.age = age
    
    '''
    类中的普通方法
    因为不需要额外的信息
    只需要传递 self 即可
    在 dog 实例化完成后
    则可以使用 dog 实例中所有属性的信息
    '''
    def sit(self) :
        print(f"{self.name.title()} is sitting.")
    
    def roll_over(self) :
        print(f"{self.name.title()} rolled over.")

'''
instance = Class(attr)
创建类的实例
定义实例名
给类的属性赋值
Python 会自动调用 __init__() 方法创建实例
'''
my_dog = Dog('huang',2);

'''
instance.attr 
创建完对象实例后
可以使用实例访问实例对象的属性
'''
print(f"my dog's name is {my_dog.name.title()} , {my_dog.age} year's old")

'''
instance.method()
创建完成对象实例后
可以用实例调用类中的方法
'''
my_dog.roll_over()
my_dog.sit()

'''
可以创建任意数量独立的实例
每个实例的属性值不同
调用类的方法将产生不同的结果
'''
hei = Dog('hei',3)
hei.roll_over()
hei.sit()


dogs = [my_dog,hei]

for dog in dogs :
    print('dog party!')
    dog.sit()
    dog.roll_over()