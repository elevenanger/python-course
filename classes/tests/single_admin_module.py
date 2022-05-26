from user_module import User

class Admin(User) :
    def __init__(self, first_name, last_name, gender,privileges):
        super().__init__(first_name, last_name, gender)
        self.privileges = privileges
    
    def show_privileges(self) :
        print("admin's privileges :")
        for privilege in self.privileges :
            print(f"\t{privilege}")