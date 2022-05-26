'''
@File    :   admin_module.py
@Time    :   2022/05/26 21:02:51
@Author  :   Liuanglin
@Desc    :   将 User 、 Privilege 、Admin 类集中存放在一个 module 中
新建一个独立的文件
创建一个 Admin 实例 调用其方法
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


class Admin(User) :
    def __init__(self, first_name, last_name, gender,privileges):
        super().__init__(first_name, last_name, gender)
        self.privileges = privileges
    
    def show_privileges(self) :
        print("admin's privileges :")
        for privilege in self.privileges :
            print(f"\t{privilege}")