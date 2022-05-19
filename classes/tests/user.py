'''
@File    :   user.py
@Time    :   2022/05/18 21:32:31
@Author  :   Liuanglin
@Desc    :   定义一个名为 User 的类
定义两个属性 first_name last_name
并创建一些其它的属性
定义 describe_user() 的方法
描述用户信息
定义 greeting_user() 向用户问好
创建多个实例
分别调用类中的所有方法 

9-5 add :
添加一个属性 login_attempts
新增方法 increment_login_attempts() 增加一次 login_attempts
新增方法 reset_login_attempts() 将 login_attempts 置为 0
'''


class User:
    
    def __init__(self,first_name,last_name,gender) :
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self) :
        if self.gender == 'male' :
            print(f'{self.first_name} {self.last_name} is a man')
        else :
            print(f'{self.first_name} {self.last_name} is a woman')
            
    def greeting_user(self) :
        if self.gender == 'male' :
            print(f'Hello Mr {self.last_name}')
        else :
            print(f'Hello Mrs {self.last_name}')
    
    def increment_login_attempts(self) :
        self.login_attempts += 1
    
    def reset_login_attempts(self) :
        self.login_attempts = 0

bond = User('james','bond','male')
beyonce = User('beyonce','knowles','female')

bond.describe_user()
bond.greeting_user()
beyonce.describe_user()
beyonce.greeting_user()

bond.increment_login_attempts()
bond.increment_login_attempts()
bond.increment_login_attempts()
bond.increment_login_attempts()
bond.increment_login_attempts()
print(bond.login_attempts)
bond.reset_login_attempts()
print(bond.login_attempts)