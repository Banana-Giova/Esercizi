from module_import1 import User

class Admin(User):
    def __init__(self, first_name: str, last_name: str, 
                    date_of_birth: str, gender: str,
                    privileges: list[str]) -> None:
        super().__init__(first_name, last_name, 
                            date_of_birth, gender)
        
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.login_attempts = 0
        self.privileges = privileges
        
    def show_privileges(self):
        privilegium:str = ''
        print("The privileges of the admin are:")
        for i in self.privileges:
            privilegium += i
            if i != self.privileges[-1]\
            and i != self.privileges:
                privilegium += ', '
            else:
                privilegium += '.'
        print(privilegium)

class Privileges:
    def __init__(self, privileges:list[str]) -> None:
        self.privileges = privileges

    def show_privileges(self):
        privilegium:str = ''
        print("The privileges of the admin are:")
        for i in self.privileges:
            privilegium += i
            if i != self.privileges[-1]\
            and i != self.privileges:
                privilegium += ', '
            else:
                privilegium += '.'
        print(privilegium)