class Restaurant:
    def __init__(self, rest_name:str, cusine_type:str,
                number_served:int=0) -> None:
        self.rest_name = rest_name
        self.cusine_type = cusine_type
        self.number_served = number_served

    def describe_restaurant(self):
        return f"{self.rest_name} is specialised "\
            f"in {self.cusine_type} and "\
            f"served {self.number_served} customers."
    
    def open_restaurant(self):
        return f"{self.rest_name} is open today!"
    
    def set_number_served(self, new_n:int):
        self.number_served = new_n

    def increment_number_served(self, increment:int):
        self.number_served += increment

class User:
    def __init__(self, first_name:str, last_name:str,
                    date_of_birth:str, gender:str) -> None:
    
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        return f"{self.first_name}, {self.last_name}, "\
                f"{self.date_of_birth}, {self.gender} | "\
                f"Login Attempts: {self.login_attempts}"
    
    def greet_user(self):
        return f"Hello {self.first_name}!"
    
    def increment_login_attempts(self, increment:int):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0