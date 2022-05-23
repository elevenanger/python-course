'''
@File    :   admin.py
@Time    :   2022/05/23 21:20:16
@Author  :   Liuanglin
@Desc    :   管理员是一种特殊的用户
定义一个类名为 Admin 继承自 User 类
添加一个属性 privileges 存储一系列的权限
写一个方法 show_privileges() 展示管理员拥有的权限
'''

from user import User
class Admin(User) :
    def __init__(self, first_name, last_name, gender,privileges):
        super().__init__(first_name, last_name, gender)
        self.privileges = privileges
    
    def show_privileges(self) :
        print("admin's privileges :")
        for privilege in self.privileges :
            print(f"\t{privilege}")

privileges = ['add menu','delete menu','bind user menu']
wong = Admin('wong','er','male',privileges)
wong.describe_user()
wong.show_privileges()